# TRANSIT & TPP

This repository contains the code and files necessary to run TRANIST and TPP. For more information see:

http://saclab.tamu.edu/essentiality/transit/transit.html

http://saclab.tamu.edu/tom/TPP.html





## Typical Mercurial Workflow
    1. Do some work until you are ready to commit or need another's changes.
    2. hg pull
    3. hg update (Note: During hg update, your uncommitted changes will be merged with the new tip of your current branch.)
    4. hg commit when ready.
    5. hg push, to push changes to bitbucket


    OR

    1. Do some work.
    2. hg commit (repeat 1 & 2 as necessary until ready to push to repository)
    2. hg pull
    3. hg merge
    4. hg commit -m "Merge"  [You will be comitting twice; you can leave the message of the second commit as "Merge"]
    5. hg push, to push changes to bitbucket





## HGRC File

An example hgrc file to setup Mercurial can be:


    [ui]
    username = FIRSTNAME LASTNAME <e-mail>

    [paths]
    default = https://USERNAME@bitbucket.org/mad-lab/transit/



You can configure mercurial to merge using your desired editor/method by adding one of the following entries to your hgrc file:
 

### Merge with conflict markers


    [ui]
    merge = internal:merge



### Merge with Emacs:

    [ui]
    merge = emacs

    [merge-tools]
    emacs.args = -q --eval "(ediff-merge-with-ancestor \""$local"\" \""$other"\" \""$base"\" nil \""$output"\")"

See the following for more information: http://mercurial.selenic.com/wiki/MergingWithEmacs



### Merge with Vi:
    [merge-tools]
    vimdiff.executable = vimdiff
    vimdiff.args = -f -d $output -M $local $base $other -c "wincmd J" -c "set modifiable" -c "set write"
    vimdiff.premerge = keep




## File directory:


* /  - Contains the TRANSIT python files

    - transit.py - main transit code.
    - transit_tools.py - global tools for reading files/data. Should be used by all methods.
    - gumbelMH.py - Gumbel method code.
    - MH_tools.py - tools used by gumbel method



* doc/ - Contains documentation (html format) for TRANSIT and TPP tools.
    - transit.html

    - TPP.html

* data/

    - Contains 5 input files (.wig format) from Griffin et al. 2011
      paper (http://www.ncbi.nlm.nih.gov/pubmed/21980284) on H37Rv
      grown on glycerol versus cholesterol.

    - Also contains represenative output files for the different
      analyses offered by TRANSIT.

* genomes/

    - Contains .fna and .prot_table files for 4 Mycobacterial organisms.
