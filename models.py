class Client:

    def __init__(self, clientName, dateAdded, clientAddress, clientCtyStZip, clientEmail):
        self.context = {}
        self.clientName = clientName
        self.context["clientName"] = clientName
        self.dateAdded = dateAdded
        self.context["dateAdded"] = dateAdded
        self.clientAddress = clientAddress
        self.context["clientAddress"] = clientAddress
        self.clientCtyStZip = clientCtyStZip
        self.context["clientCtyStZip"] = clientCtyStZip
        self.clientEmail = clientEmail
        self.context["clientEmail"] = clientEmail

class Materials:

    def __init__(self, def_name, case_number, judge, date_of_today):
        self.context = {}
        self.def_name = def_name
        self.context["def_name"] = def_name
        self.case_number = case_number
        self.context["case_number"] = case_number
        self.judge = judge
        self.context["judge"] = judge
        self.date_of_today = date_of_today
        self.context["date_of_today"] = date_of_today

class ClientService(Client):
    def __init__(self, Client,lawyerAssigned, servicesRequested, clientFee, clientBalance, estimatedTimeFrame, mattersDescription):
        self.lawyerAssigned = lawyerAssigned
        self.servicesRequested = servicesRequested
        self.clientFee = clientFee
        self.clientBalance = clientBalance
        self.estimatedTimeFrame = estimatedTimeFrame
        self.mattersDescription = mattersDescription

class ClientCase(ClientService):
    def __init__(self, clientServices, caseNumber):
        self.clientServices = clientServices
        self.caseNumber = caseNumber
