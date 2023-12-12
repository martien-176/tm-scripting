# Lists projects a mapper joined, including number of mapped and validated tasks

#!/usr/bin/python3

import json
import sys
import urllib.parse
import urllib.request
from termcolor import colored


def main():

    if len (sys.argv) == 2:
        user = sys.argv[1]
    else:
        print ("Usage: hot_tm_get_user_projects <username>")
        return 1

    req = urllib.request.Request ("https://" + urllib.parse.quote ("tasking-manager-tm4-production-api.hotosm.org/api/v2/projects/queries/" + user + "/touched/"),
                                  headers={"accept": "application/json", "Accept-Language": "en"}
                                 )
    with urllib.request.urlopen (req) as response:
        res = json.loads (response.read ())

    if "Error" in res:
        print (res["Error"])
        return 1

    if len (res["mappedProjects"]) < 0:
        print ("no projects mapped or validated so far")
        return 1

    for proj in res["mappedProjects"]:
        print ("--------------------------------------")
        print (proj["projectId"], ": ", proj["name"])
        print (colored("    https://tasks.hotosm.org/projects/" + str(proj["projectId"]), "green"))
        print ("    mapped ", proj["tasksMapped"])
        if proj["tasksValidated"] > 0:
            print (colored("    validated " + str(proj["tasksValidated"]), "red"))
        else:
            print ("    validated: NONE")


if __name__ == "__main__":
    main()
    

