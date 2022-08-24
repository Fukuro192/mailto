"""
A library with a single function to use: the mailto function.
"""

from urllib.parse import quote as to_uri # for converting text to URL syntax

def param_delim(cc: str = "", bcc: str = "", subject: str = "", body: str = ""):
	"""
	returns the URL parameter delimiter '?' if
	any of the arguments are not empty and not NoneType.
	"""
	if ( cc != "" and cc is not None):
		return "?"
	if ( bcc != "" and bcc is not None):
		return "?"
	if ( subject != "" and subject is not None):
		return "?"
	if ( body != "" and body is not None):
		return "?"
	return ""

def mailto_href(*mail_args, cc: str = "", bcc: str = "", subject: str = "", body: str = ""):
	"""
	Generates the necessary string to be added in
	the href attribute of the <a>-tag in HTML.
	"""

	_mail_args = [mail for mail in mail_args if mail is not None]
	_cc = cc if cc is not None else ""
	_bcc = bcc if bcc is not None else ""
	_subject = to_uri(subject) if subject is not None else ""
	_body = to_uri(body) if body is not None else ""
	
	# setting the url_mail to strating point "mailto:"
	url_mail_str = "mailto:"

	# adding the main mails
	for mail in _mail_args:
		url_mail_str += mail
		if mail != _mail_args[-1]:
			url_mail_str += ";"

	# adding parameter delimiter '?' if necessary
	url_mail_str += param_delim(cc=_cc, bcc=_bcc, subject=_subject, body=_body)

	# adding cc
	if ( _cc != "" ):
		url_mail_str += "cc=" + _cc
	# adding bcc
	if ( _bcc != "" ):
		if ( _cc != "" ):
			url_mail_str += "&"
		url_mail_str += "bcc=" + _bcc
	# adding subject
	if ( _subject != "" ):
		if ( _cc != "" or _bcc != "" ):
			url_mail_str += "&"
		url_mail_str += "subject=" + _subject
	# adding body
	if ( _body != "" ):
		if ( _cc != "" or _bcc != "" or _subject != "" ):
			url_mail_str += "&"
		url_mail_str += "body=" + _body

	# return the final result
	return url_mail_str