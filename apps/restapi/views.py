# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import spotipy, spotipy.oauth2 as oauth2, spotipy.util as util

# client_id='2cd4585c7abf46a1b570a60af54e4620',client_secret='c83d25b0ef8f4db9b8300d0eea6aa1b9'

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def swap(request):
	sp = oauth2.SpotifyOAuth(client_id='2cd4585c7abf46a1b570a60af54e4620',client_secret='c83d25b0ef8f4db9b8300d0eea6aa1b9',redirect_uri='Audial://returnAfterLogin')

	return HttpResponse(sp.get_access_token('BQAQV5tgid78qx_N11RwDZiA1WzgckV2-XZ03f7bxvzKiCV5qqkDGapNfBdqpGSFb6TqlE8yK7AdnFTEPFr4tIVuBxHoIts32Soe8VdQJJMEaXijYxTO79kHaxMjpnorvpkNTpuATbS66oTxZc4wFLUPINLlDGdnoSPDZ0Nyv22eWBLJlbIsp0kzSc-ywJ95kb6G4ZDoDcSlK4WLZ-kT3bNEcrMSXGnU4SaTeXjOa2kxO24U6rD58fz4C7f0ZyZGewVU2K6zRccLGg'))

def refresh(request):
	return render(request, 'tokenExchange/refresh.html')



	XZ03f7bxvzKiCV5qqkDGapNfBdqpGSFb6TqlE8yK7AdnFTEPFr4tIVuBxHoIts32Soe8VdQJJMEaXijYxTO79kHaxMjpnorvpkNTpuATbS66oTxZc4wFLUPINLlDGdnoSPDZ0Nyv22eWBLJlbIsp0kzSc-ywJ95kb6G4ZDoDcSlK4WLZ-kT3bNEcrMSXGnU4SaTeXjOa2kxO24U6rD58fz4C7f0ZyZGewVU2K6zRccLGg

	BQAtYfbj0TcPjTlsx8e1d5F5HsNFIY5VFkoiWPQRwtedyoDeULDNogWrMwXitu-koD8UdrAufJiEG62mj28hbw