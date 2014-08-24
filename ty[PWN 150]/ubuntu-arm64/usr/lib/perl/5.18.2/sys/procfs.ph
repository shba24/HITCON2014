require '_h2ph_pre.ph';

no warnings qw(redefine misc);

unless(defined(&_SYS_PROCFS_H)) {
    eval 'sub _SYS_PROCFS_H () {1;}' unless defined(&_SYS_PROCFS_H);
    require 'features.ph';
    require 'sys/time.ph';
    require 'sys/types.ph';
    require 'sys/user.ph';
    require 'asm/ptrace.ph';
    undef(&PTRACE_GET_THREAD_AREA) if defined(&PTRACE_GET_THREAD_AREA);
    undef(&PTRACE_GETHBPREGS) if defined(&PTRACE_GETHBPREGS);
    undef(&PTRACE_SETHBPREGS) if defined(&PTRACE_SETHBPREGS);
    require 'sys/user.ph';
    eval 'sub ELF_NGREG () {($sizeof{\'struct user_pt_regs\'} / $sizeof{ &elf_greg_t});}' unless defined(&ELF_NGREG);
    eval 'sub ELF_PRARGSZ () {(80);}' unless defined(&ELF_PRARGSZ);
}
1;
