#!/usr/bin/env python
from django.core.management import execute_manager
import openshift.settings

if __name__ == "__main__":
    execute_manager(openshift.settings)
