require '_h2ph_pre.ph';

no warnings qw(redefine misc);

unless(defined(&__ASM_SIGCONTEXT_H)) {
    eval 'sub __ASM_SIGCONTEXT_H () {1;}' unless defined(&__ASM_SIGCONTEXT_H);
    require 'linux/types.ph';
    eval 'sub FPSIMD_MAGIC () {0x46508001;}' unless defined(&FPSIMD_MAGIC);
}
1;
