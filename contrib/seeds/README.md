### Seeds ###

Utility to generate the seeds.txt list that is compiled into the client
(see [src/chainparamsseeds.h](/src/chainparamsseeds.h) and other utilities in [contrib/seeds](/contrib/seeds)).

Dependency: apt-get install python3-dnspython

The seeds compiled into the release are created from sipa's DNS seed data, like this:

    fill in mue_seeds.txt
    python makeseeds.py < mue_seeds.txt > nodes_main.txt
    python generate-seeds.py . > ../../src/chainparamsseeds.h

