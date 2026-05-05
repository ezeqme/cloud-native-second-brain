---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "101 Track"
themes: ["101 Track"]
speakers: ["Quentin Monnet", "Isovalent"]
sched_url: https://kccnceu2021.sched.com/event/iE5N/ebpf-on-the-rise-getting-started-quentin-monnet-isovalent
youtube_search_url: https://www.youtube.com/results?search_query=eBPF+on+the+Rise+-+Getting+Started+CNCF+KubeCon+2021
slides: []
status: parsed
---

# eBPF on the Rise - Getting Started - Quentin Monnet, Isovalent

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[101 Track]]
- Temas: [[101 Track]]
- País/cidade: Virtual / Virtual
- Speakers: Quentin Monnet, Isovalent
- Schedule: https://kccnceu2021.sched.com/event/iE5N/ebpf-on-the-rise-getting-started-quentin-monnet-isovalent
- Busca YouTube: https://www.youtube.com/results?search_query=eBPF+on+the+Rise+-+Getting+Started+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre eBPF on the Rise - Getting Started.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE5N/ebpf-on-the-rise-getting-started-quentin-monnet-isovalent
- YouTube search: https://www.youtube.com/results?search_query=eBPF+on+the+Rise+-+Getting+Started+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=cABk-6Sdb20
- YouTube title: eBPF on the Rise - Getting Started - Quentin Monnet, Isovalent
- Match score: 0.799
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/ebpf-on-the-rise-getting-started/cABk-6Sdb20.txt
- Transcript chars: 24328
- Keywords: ebpf, kernel, program, number, programs, already, available, trace, everything, packets, networking, applications, security, native, process, implement, network, processing

### Resumo baseado na transcript

hi everyone thank you for attending my presentation called ebpf on the rise i'm quentin i work as a software engineer at isovalent and we are doing cdm which is built on top of ebpf to bring networking observability and security to kubernetes clusters my objective today is to help you getting started with ebpf and we'll do that in three parts the first section will be about understanding how ebpf works and then in a second time we'll see what tools are available for working with ebpf and the

### Excerpt da transcript

hi everyone thank you for attending my presentation called ebpf on the rise i'm quentin i work as a software engineer at isovalent and we are doing cdm which is built on top of ebpf to bring networking observability and security to kubernetes clusters my objective today is to help you getting started with ebpf and we'll do that in three parts the first section will be about understanding how ebpf works and then in a second time we'll see what tools are available for working with ebpf and the last section will be about what benefits we can have for cloud native environments uh from ebpf so before we dive into the details let's observe that there is something happening with ebps tuesdays it's been marked by liz rice as one of the key technologies to watch for this year but why is that so what what's happening with ebpf to really understand that let's observe that the linux system is being used at the basis for everything in cloud environments nowadays and we have some kind of paradox with linux because everything that allows you to get some observability to understand what resources are used by a given process of pod is happening on the kernel side but you have very little flexibility at the center in the kernel you are free to program whatever you want in user space but in user space you won't get a direct access to those kernel data structures so do we have a way to introduce more programmability in the kernel we have kindle modules but kernel modules can be tricky to implement or they can have issues in terms of safety you are likely to uh crash your kernel if you made some insects some mistakes in your modules you do not have any guarantees in terms of api stability from the canal from one version to the other one so that can break your modules too uh so we have those all those kind of components that are like bounded box uh in which you can you can work with from which you can um interact but can you somehow get out of the box and bring back some programmability into the kernel not at the expense of safety or efficiency and if so can you leverage that to get some benefits in your cloud native environments the answer of course is ebpf so ebpf is some generic purpose execution engine to already implement your programs defined in user space inside of the kernel so historically it was built on top of what is now called the classic bpf which was used with this pinum or second uh to filter packets to computer user space or cisco arguments uh respectively and
