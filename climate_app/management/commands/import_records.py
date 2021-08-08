# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

import csv
import datetime
import logging

from pprint import pprint

from climate_app.models import DACMemberCountry
from climate_app.models import InitialModel


class Command(BaseCommand):
    def handle(self, **options):
        encoding = "utf-8"
        file_path = "C:/Django/ICSC/climate-tagging-ph/fixtures/dac_sample.csv"
        with open(file_path, "rt", encoding=encoding) as csv_file_input:
            csv_reader = csv.reader(csv_file_input, delimiter=",")
            line_count = 0

            DACMemberCountry.objects.all().delete()

            for row in csv_reader:
                if line_count == 0:
                    print("\nCOLUMN HEADERS:\n", (": ".join(row)))
                    line_count += 1

                else:
                    pprint("")
                    pprint("ROW NUMBER: %s" % line_count)

                    if row[0] != "":
                        country_code = row[0]
                        year = row[1]
                        provider_type = row[2]
                        provider = row[3]
                        provider_code = row[4]
                        adaptation_objective = row[5]
                        mitigation_objective = row[6]
                        adaptation_dev_finance_commitment_2019 = row[8]
                        adaptation_dev_finance_commitment_current = row[7]
                        mitigation_dev_finance_commitment_2019 = row[10]
                        mitigation_dev_finance_commitment_current = row[9]
                        overlap_commitment_2019 = row[12]
                        overlap_commitment_current = row[11]
                        climate_dev_finance_commitment_2019 = row[14]
                        climate_dev_finance_commitment_current = row[13]
                        channel_delivery_code = row[15]
                        channel_delivery = row[16]
                        purpose_code = row[17]
                        sector = row[18]
                        sub_sector = row[19]
                        development_cooperation_modality = row[20]
                        financial_instrument = row[21]
                        finance_type = row[22]
                        gender = row[23]

                        country_code_value = InitialModel.objects.get(
                            country_code=int(country_code)
                        )
                        record = DACMemberCountry(
                            country_code=country_code_value,
                            year=year,
                            provider_type=provider_type,
                            provider=provider,
                            provider_code=provider_code,
                            adaptation_objective=adaptation_objective,
                            mitigation_objective=mitigation_objective,
                            adaptation_dev_finance_commitment_2019=adaptation_dev_finance_commitment_2019,
                            adaptation_dev_finance_commitment_current=adaptation_dev_finance_commitment_current,
                            mitigation_dev_finance_commitment_2019=mitigation_dev_finance_commitment_2019,
                            mitigation_dev_finance_commitment_current=mitigation_dev_finance_commitment_current,
                            overlap_commitment_2019=overlap_commitment_2019,
                            overlap_commitment_current=overlap_commitment_current,
                            climate_dev_finance_commitment_2019=climate_dev_finance_commitment_2019,
                            climate_dev_finance_commitment_current=climate_dev_finance_commitment_current,
                            channel_delivery_code=channel_delivery_code,
                            channel_delivery=channel_delivery,
                            purpose_code=purpose_code,
                            sector=sector,
                            sub_sector=sub_sector,
                            development_cooperation_modality=development_cooperation_modality,
                            financial_instrument=financial_instrument,
                            finance_type=finance_type,
                            gender=gender,
                        )
                        record.save()
                        line_count += 1
                        pprint(provider + " CREATED!")
                        pprint("#" * 70)
                    else:
                        return False

                logging.info(
                    "PROCESSED -'%s' LINES. OECD DATA IMPORT SUCCESS."
                    % (int(line_count) - 1)
                )
        csv_file_input.close()
