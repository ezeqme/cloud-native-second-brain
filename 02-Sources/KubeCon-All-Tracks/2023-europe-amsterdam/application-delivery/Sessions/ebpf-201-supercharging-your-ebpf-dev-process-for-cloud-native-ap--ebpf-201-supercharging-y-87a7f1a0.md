---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Application + Delivery"
themes: ["GitOps Delivery"]
speakers: ["Sanjeev Rampal", "Donald Hunter", "Red Hat"]
sched_url: https://kccnceu2023.sched.com/event/1Hycp/ebpf-201-supercharging-your-ebpf-dev-process-for-cloud-native-apps-sanjeev-rampal-donald-hunter-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=eBPF+201%3A+Supercharging+Your+eBPF+Dev+Process+for+Cloud+Native+Apps+CNCF+KubeCon+2023
slides: []
status: parsed
---

# eBPF 201: Supercharging Your eBPF Dev Process for Cloud Native Apps - Sanjeev Rampal & Donald Hunter, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Application + Delivery]]
- Temas: [[GitOps Delivery]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Sanjeev Rampal, Donald Hunter, Red Hat
- Schedule: https://kccnceu2023.sched.com/event/1Hycp/ebpf-201-supercharging-your-ebpf-dev-process-for-cloud-native-apps-sanjeev-rampal-donald-hunter-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=eBPF+201%3A+Supercharging+Your+eBPF+Dev+Process+for+Cloud+Native+Apps+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre eBPF 201: Supercharging Your eBPF Dev Process for Cloud Native Apps.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hycp/ebpf-201-supercharging-your-ebpf-dev-process-for-cloud-native-apps-sanjeev-rampal-donald-hunter-red-hat
- YouTube search: https://www.youtube.com/results?search_query=eBPF+201%3A+Supercharging+Your+eBPF+Dev+Process+for+Cloud+Native+Apps+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=9vUJhbqf4eo
- YouTube title: eBPF 201: Supercharging Your eBPF Dev Process for Cloud Native Apps - Sanjeev Rampal & Donald Hunter
- Match score: 0.9
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/ebpf-201-supercharging-your-ebpf-dev-process-for-cloud-native-apps/9vUJhbqf4eo.txt
- Transcript chars: 29343
- Keywords: kernel, program, programs, within, features, packet, access, development, modern, available, application, support, write, little, getting, version, perspective, running

### Resumo baseado na transcript

my name's Donald Hunter I'm from the emerging Tech Team in red hat I'm my colleague Sanjeev couldn't unfortunately make it for personal reasons so I'll take this one on my own and so let's get started this is a ebpf 201 and the goal of this talk really is just to um well assume that everybody knows what ebpf is so we're not going to do the ebpf101 but we're going to provide some guidelines I guess for how to get started in in larger project development with BPF

### Excerpt da transcript

my name's Donald Hunter I'm from the emerging Tech Team in red hat I'm my colleague Sanjeev couldn't unfortunately make it for personal reasons so I'll take this one on my own and so let's get started this is a ebpf 201 and the goal of this talk really is just to um well assume that everybody knows what ebpf is so we're not going to do the ebpf101 but we're going to provide some guidelines I guess for how to get started in in larger project development with BPF and really the goal here is to Target people that are not kernel developers people like yourselves in the room who are kubernetes developers primarily I guess and maybe somewhat unfamiliar with some of the Linux kernel development practices so we're slightly past the BBF 101 as I said um and we're going to focus on how we might tackle writing maintainable portable programs that can be installed into the kernel and this is kind of based on our experiences of learning as newbies as we went along so hopefully what I present here will be helpful to anybody that's um starting on a BPF programming Journey so just before I get started can I get a show of hands of people that know what BPF is okay most of you that's good and the show of hands of people that um have actually programmed some BPF code yeah are considerably smaller number that's I guess to be expected um have people installed BPF programs and used them for observability in their clusters yep a reasonable number okay so that kind of level sets what the audience expectations might be from the from the talk okay so I'm gonna recap a little bit on BPF not right from the beginnings but just modern BPF as it stands today give you an overview of what I think are the kind of applications that can benefit from using BPF I'll give you a bit of an overview of the technology and uh the the tools available in modern BPF and then for the second half the presentation go through some what I would describe development best practices and then at the end of that we'll talk about a few kubernetes specifics okay so just a technology introduction first so BPF is if for anybody that's not familiar with it it's a Sandbox virtual machine environment inside the Linux kernel um which has a verifier that checks whether or not your program will safely run to completion inside the kernel without causing any hiccups so if your program doesn't pass the verifier it doesn't even get installed into the kernel if your program does pass the verifier then it can be attached to one
