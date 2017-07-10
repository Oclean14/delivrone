from time import gmtime, strftime

class Log:
	# flags disponible pour les logs
	LOG_INFO_ENABLE = 1 << 0
	LOG_DEBUG_ENABLE = 1 << 1
	LOG_WARNING_ENABLE = 1 << 2
	LOG_ERROR_ENABLE = 1 << 3
	LOG_ALL_ENABLE = 15
	# variable a setter avec les valeurs ci-dessus pour choisir quel type de log afficherflags = 0
	flags = 0

	@staticmethod
	def debug(tag, msg):
		if Log.flags & Log.LOG_DEBUG_ENABLE:
			print strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "[ DEBUG ][ " + tag + " ] " +  msg

	@staticmethod
	def info(tag, msg):
		if Log.flags & Log.LOG_INFO_ENABLE:
			print strftime("%Y-%m-%d %H:%M:%S", gmtime()) +  "[ INFO ][ " + tag, " ] " +  msg

	@staticmethod
	def error(tag, msg):
		if Log.flags & Log.LOG_ERROR_ENABLE:
			print strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "[ ERROR ][ " + tag + " ] " + msg

	@staticmethod
	def warning(tag,msg):
		if Log.flags & Log.LOG_WARNING_ENABLE:
			print strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "[ WARNING ][ " + tag + " ] " + msg
