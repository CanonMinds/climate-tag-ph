from django.db import models

# Create your models here.
class InitialModel(models.Model):
    country_code = models.IntegerField("Country Code", default=0, blank=True, null=True)
    sovereignty = models.CharField(max_length=100, null=False)
    geometry = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"
        ordering = ["country_code"]

    def __str__(self):
        return "{} - {}".format(self.country_code, self.sovereignty)


class DACMemberCountry(models.Model):
    country_code = models.ForeignKey(
        InitialModel, on_delete=models.CASCADE, null=True, blank=True, related_name="+"
    )
    year = models.IntegerField("Year", default=0, blank=False, null=True)
    provider_type = models.CharField("Provider Type", max_length=200, blank=True)
    provider = models.CharField("Provider", max_length=200, blank=False)
    provider_code = models.IntegerField(
        "Provider Code", default=0, blank=True, null=True
    )
    adaptation_objective = models.CharField(
        "Adaptation Objective (applies to Rio-marked data only)",
        max_length=200,
        blank=True,
    )
    mitigation_objective = models.CharField(
        "Mitigation Objective", max_length=200, blank=True
    )

    adaptation_dev_finance_commitment_2019 = models.DecimalField(
        "Adaptation-related Development Finance Commitment (2019)",
        default=0,
        max_digits=19,
        decimal_places=10,
        null=True,
        blank=False,
    )
    adaptation_dev_finance_commitment_current = models.DecimalField(
        "Adaptation-related Development Finance Commitment (current)",
        default=0,
        max_digits=19,
        decimal_places=10,
        null=True,
        blank=False,
    )
    mitigation_dev_finance_commitment_2019 = models.DecimalField(
        "Mitigation-related Development Finance Commitment (2019)",
        default=0,
        max_digits=19,
        decimal_places=10,
        null=True,
        blank=False,
    )
    mitigation_dev_finance_commitment_current = models.DecimalField(
        "Mitigation-related Development Finance Commitment (current)",
        default=0,
        max_digits=19,
        decimal_places=10,
        null=True,
        blank=False,
    )
    overlap_commitment_2019 = models.DecimalField(
        "Overlap Commitment (2019)",
        default=0,
        max_digits=19,
        decimal_places=10,
        null=True,
        blank=False,
    )
    overlap_commitment_current = models.DecimalField(
        "Overlap Commitment (current)",
        default=0,
        max_digits=19,
        decimal_places=10,
        null=True,
        blank=False,
    )
    climate_dev_finance_commitment_2019 = models.DecimalField(
        "Climate-related Development Finance Commitment (2019)",
        default=0,
        max_digits=19,
        decimal_places=10,
        null=True,
        blank=False,
    )
    climate_dev_finance_commitment_current = models.DecimalField(
        "Climate-related Development Finance Commitment (current)",
        default=0,
        max_digits=19,
        decimal_places=10,
        null=True,
        blank=False,
    )

    channel_delivery_code = models.IntegerField(
        "Channel of Delivery Code", default=0, blank=True, null=True
    )
    channel_delivery = models.CharField(
        "Channel of Delivery", max_length=200, blank=True
    )
    purpose_code = models.IntegerField("Purpose Code", default=0, blank=True, null=True)
    sector = models.CharField("Sector (detailed)", max_length=200, blank=True)
    sub_sector = models.CharField("Sub-sector", max_length=200, blank=True)
    development_cooperation_modality = models.CharField(
        "Development of Cooperation Modality", max_length=200, blank=True
    )
    financial_instrument = models.CharField(
        "Financial Instrument", max_length=200, blank=True
    )
    finance_type = models.IntegerField(
        "Type of Finance", default=0, blank=True, null=True
    )
    gender = models.CharField("Gender", max_length=200, blank=True)
    is_published = models.BooleanField("Publish", default=True)
    class Meta:
        verbose_name = "DACMemberCountry"
        verbose_name_plural = "DACMemberCountries"

    def __str__(self):
        return self.provider
