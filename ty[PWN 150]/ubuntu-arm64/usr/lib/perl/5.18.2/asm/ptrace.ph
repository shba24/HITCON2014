require '_h2ph_pre.ph';

no warnings qw(redefine misc);

unless(defined(&__ASM_PTRACE_H)) {
    eval 'sub __ASM_PTRACE_H () {1;}' unless defined(&__ASM_PTRACE_H);
    require 'linux/types.ph';
    require 'asm/hwcap.ph';
    eval 'sub PSR_MODE_EL0t () {0x;}' unless defined(&PSR_MODE_EL0t);
    eval 'sub PSR_MODE_EL1t () {0x4;}' unless defined(&PSR_MODE_EL1t);
    eval 'sub PSR_MODE_EL1h () {0x5;}' unless defined(&PSR_MODE_EL1h);
    eval 'sub PSR_MODE_EL2t () {0x8;}' unless defined(&PSR_MODE_EL2t);
    eval 'sub PSR_MODE_EL2h () {0x9;}' unless defined(&PSR_MODE_EL2h);
    eval 'sub PSR_MODE_EL3t () {0xc;}' unless defined(&PSR_MODE_EL3t);
    eval 'sub PSR_MODE_EL3h () {0xd;}' unless defined(&PSR_MODE_EL3h);
    eval 'sub PSR_MODE_MASK () {0xf;}' unless defined(&PSR_MODE_MASK);
    eval 'sub PSR_MODE32_BIT () {0x10;}' unless defined(&PSR_MODE32_BIT);
    eval 'sub PSR_F_BIT () {0x40;}' unless defined(&PSR_F_BIT);
    eval 'sub PSR_I_BIT () {0x80;}' unless defined(&PSR_I_BIT);
    eval 'sub PSR_A_BIT () {0x100;}' unless defined(&PSR_A_BIT);
    eval 'sub PSR_D_BIT () {0x200;}' unless defined(&PSR_D_BIT);
    eval 'sub PSR_Q_BIT () {0x8000000;}' unless defined(&PSR_Q_BIT);
    eval 'sub PSR_V_BIT () {0x10000000;}' unless defined(&PSR_V_BIT);
    eval 'sub PSR_C_BIT () {0x20000000;}' unless defined(&PSR_C_BIT);
    eval 'sub PSR_Z_BIT () {0x40000000;}' unless defined(&PSR_Z_BIT);
    eval 'sub PSR_N_BIT () {0x80000000;}' unless defined(&PSR_N_BIT);
    eval 'sub PSR_f () {0xff000000;}' unless defined(&PSR_f);
    eval 'sub PSR_s () {0xff0000;}' unless defined(&PSR_s);
    eval 'sub PSR_x () {0xff00;}' unless defined(&PSR_x);
    eval 'sub PSR_c () {0xff;}' unless defined(&PSR_c);
    unless(defined(&__ASSEMBLY__)) {
    }
}
1;
