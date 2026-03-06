import ssl
import smtplib
from django.core.mail.backends.smtp import EmailBackend


class NoVerifyEmailBackend(EmailBackend):
    """Backend SMTP sans vérification du certificat SSL (développement Windows)."""

    def open(self):
        if self.connection:
            return False

        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE

        try:
            self.connection = smtplib.SMTP(
                self.host,
                self.port,
                timeout=self.timeout or None,
            )
            self.connection.ehlo()
            if self.use_tls:
                self.connection.starttls(context=ssl_context)
                self.connection.ehlo()
            if self.username and self.password:
                self.connection.login(self.username, self.password)
            return True
        except Exception:
            if not self.fail_silently:
                raise
