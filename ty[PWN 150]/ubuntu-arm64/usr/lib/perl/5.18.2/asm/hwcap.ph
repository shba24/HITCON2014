require '_h2ph_pre.ph';

no warnings qw(redefine misc);

unless(defined(&__ASM_HWCAP_H)) {
    eval 'sub __ASM_HWCAP_H () {1;}' unless defined(&__ASM_HWCAP_H);
    eval 'sub HWCAP_FP () {(1<< 0);}' unless defined(&HWCAP_FP);
    eval 'sub HWCAP_ASIMD () {(1<< 1);}' unless defined(&HWCAP_ASIMD);
    eval 'sub HWCAP_EVTSTRM () {(1<< 2);}' unless defined(&HWCAP_EVTSTRM);
}
1;
