#!/usr/bin/env python
import logging

def l

def log2()
	logging.basicConfig(
												level				=		logging.WARNING	,
												format			=		"[%(levelname)s] %(message)s"	,
												handlers		=		[
																					logging.FileHandler("global.log")	,
																					logging.StreamHandler()	,
																				],
											)
log