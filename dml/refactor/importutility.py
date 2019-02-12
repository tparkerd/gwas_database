#!/usr/bin/env python
"""Utility methods for import.py"""
from dbconnect import connect
import find
from datetime import datetime as dt
import pandas as pd
import numpy as np
import psycopg2
import csv
import insert
from dbconnect import config, connect
from models import species, population, line, chromosome, variant, genotype, trait, phenotype, growout_type, growout, location, gwas_algorithm, genotype_version, imputation_method, kinship_algorithm, kinship, population_structure_algorithm, population_structure, gwas_run, gwas_result


def growout_name_to_year(value):
  """Takes in a LOYR (Location-Year) string and converts year digits to four-digit year"""
  # Pre-cleaning
  value = value.strip()
  try:
    if len(value) < 4:
      return None
    else:
      prefix = value[:2]
      suffix = value[-2:]
      current_year_suffix = str(dt.now().year)[-2:]
      # Assume if the last two digits are greater than those of the current year,
      # then we are working in the previous millennium
      if int(suffix) > int(current_year_suffix):
        value = f"19{suffix}"
      else:
        value = f"20{suffix}"
      return value
  except:
    return None

def create_location(code):
  """Creates a location object from user-input
  
  :param code: unique name for location
  :type code: str
  :return: location
  :rtype: dict
  """
  location = {}
  location["country"] = input(f"Location country (required): ") or None
  location["state"] = input(f"Location state: ") or ""
  location["city"] = input(f"Location city: ") or ""
  location["code"] = input(f"Location code (required, must be unique): ") or None
  while location["country"] is None:
    location["country"] = input(f"Country must be identified. Please enter a country for the location: ") or None
  while location["code"] is None:
    location["code"] = input(f"A location code must be provided. Please enter a location code for the location: ") or None

  # The code is finally defined, so we need to validate if the code can be
  # used.
  conn = connect()
  # Was it already claimed? If so, does it match... If it matches, great! Don't create it.
  validate.location_exists(conn, location)

  location_id = find.find_location(conn, location["code"])
  # Location by code not in database, create a new one
  if location_id is None:



  
  return 
