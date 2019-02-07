#include <cstdlib>
#include <iostream>
#include <libsnmp.h>

#include "snmp_pp/snmp_pp.h"

using namespace Snmp_pp;

int main()
{
    int status; 
    Snmp::socket_startup();  // Initialize socket subsystem
    Snmp snmp(status);                // check construction status
    if (status != SNMP_CLASS_SUCCESS)
    {
        std::cout << "SNMP++ Session Create Fail, " << snmp.error_msg(status) << "\n";
        return 1;
    }
}
