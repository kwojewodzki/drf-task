import uuid
from django.core import signing
from django.urls import reverse
import time
from .models import ExpiringLink
from rest_framework.exceptions import NotFound


class ExpiringLinkMixin:
    def generate_expiring_link(self, image, time_to_expired):
        """Generates expiring link from uploaded image."""
        pk = uuid.uuid4()
        signed_link = signing.dumps(str(pk))

        full_url = self.request.build_absolute_uri(reverse('expiring_link_detail', kwargs={'signed_link': signed_link}))

        current_time = int(time.time())
        expiry_time = current_time + int(time_to_expired)

        ExpiringLink.objects.create(id=pk, link=full_url, image=image, time_to_expired=expiry_time)

        return {'link': full_url}

    @staticmethod
    def decode_signed_value(value):
        """Decodes signed link."""
        try:
            return signing.loads(value)
        except signing.BadSignature:
            raise NotFound('Invalid signed link')