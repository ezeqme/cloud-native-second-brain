---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Performance"
themes: ["SRE Reliability"]
speakers: ["Frederic Branczyk", "Polar Signals"]
sched_url: https://kccncna2021.sched.com/event/lV6D/beyond-the-hype-cloud-native-ebpf-frederic-branczyk-polar-signals
youtube_search_url: https://www.youtube.com/results?search_query=Beyond+the+Hype%3A+Cloud+Native+eBPF+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Beyond the Hype: Cloud Native eBPF - Frederic Branczyk, Polar Signals

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Performance]]
- Temas: [[SRE Reliability]]
- País/cidade: United States / Los Angeles
- Speakers: Frederic Branczyk, Polar Signals
- Schedule: https://kccncna2021.sched.com/event/lV6D/beyond-the-hype-cloud-native-ebpf-frederic-branczyk-polar-signals
- Busca YouTube: https://www.youtube.com/results?search_query=Beyond+the+Hype%3A+Cloud+Native+eBPF+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Beyond the Hype: Cloud Native eBPF.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV6D/beyond-the-hype-cloud-native-ebpf-frederic-branczyk-polar-signals
- YouTube search: https://www.youtube.com/results?search_query=Beyond+the+Hype%3A+Cloud+Native+eBPF+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2rdNCn_JXYk
- YouTube title: Beyond the Hype: Cloud Native eBPF - Frederic Branczyk, Polar Signals
- Match score: 0.753
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/beyond-the-hype-cloud-native-ebpf/2rdNCn_JXYk.txt
- Transcript chars: 24997
- Keywords: ebpf, essentially, kernel, program, actually, process, programs, container, profiling, information, compile, traces, containers, native, signals, called, little, particular

### Resumo baseado na transcript

i'm frederick i'm the founder of polar signals and today we want to talk about cloud native ebpf beyond the hype as you can probably imagine we use ebpf at polar signals and that's essentially why i'm here but the idea of this talk is to kind of take this technology this hit that has been hyped over the last couple of years and see how we can kind of connect it in a meaningful way to the cloud native ecosystem to create some useful things so hopefully you'll walk

### Excerpt da transcript

i'm frederick i'm the founder of polar signals and today we want to talk about cloud native ebpf beyond the hype as you can probably imagine we use ebpf at polar signals and that's essentially why i'm here but the idea of this talk is to kind of take this technology this hit that has been hyped over the last couple of years and see how we can kind of connect it in a meaningful way to the cloud native ecosystem to create some useful things so hopefully you'll walk out of this talk understanding ebpf a little bit more understanding uh kind of the the state of development with ebpf a little bit more and lastly um how to connect potential ebpf programs with the kubernetes or cloud native ecosystem more broadly and i'll show an example of what that could potentially look like so without further ado let's have a really quick introduction to ebpf now this won't be completely exhaustive of an explanation but i just want to lay a little bit of kind of information down so that as we progress in the talk we have a foundation that we can work off of so essentially what is ebpf ebpf allows us to run certain programs in kernel space and we can attach these programs to particular events or hooks so some things that people may be familiar with are k-probes or u-probes essentially what you're saying is you wanna run this program every time a particular thing happens in the kernel for example a syscall gets executed and the reason why we do this is so that we don't have this really expensive context switch when we whenever we go from kernel space to user space this is a like widely known fact that this transition is like something really expensive and the reason why we're doing this as well ebpf or the kernel and the operating system has traditionally always been a really great place to do observability security and networking but uh the reason why ebpf was necessary here was that with ebpf we can now have a really flexible development model where we hot load this this code into the kernel and execute it as part of kernel space without having to you know load a kernel module which we had to compile to a wide array wide array of architectures and kernels and so on um and even even though it used to be really hard some companies even still did that right like cystic started that way um and um only eventually when ebpf came around uh adopted ebpf as a technology so sometimes it was even then already worth it but with ebpf we're kind of um supercharging this possibility and i j
