---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Security"
themes: ["Security"]
speakers: ["Natalia Reka Ivanko", "Duffie Cooley", "Isovalent @ Cisco"]
sched_url: https://kccncna2024.sched.com/event/1i7qb/seccomp-and-ebpf-whats-the-difference-why-do-i-need-to-know-natalia-reka-ivanko-duffie-cooley-isovalent-cisco
youtube_search_url: https://www.youtube.com/results?search_query=Seccomp+and+eBPF%3B+What%E2%80%99s+the+Difference%3F+Why+Do+I+Need+to+Know%3F+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Seccomp and eBPF; What’s the Difference? Why Do I Need to Know? - Natalia Reka Ivanko & Duffie Cooley, Isovalent @ Cisco

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]]
- País/cidade: United States / Salt Lake City
- Speakers: Natalia Reka Ivanko, Duffie Cooley, Isovalent @ Cisco
- Schedule: https://kccncna2024.sched.com/event/1i7qb/seccomp-and-ebpf-whats-the-difference-why-do-i-need-to-know-natalia-reka-ivanko-duffie-cooley-isovalent-cisco
- Busca YouTube: https://www.youtube.com/results?search_query=Seccomp+and+eBPF%3B+What%E2%80%99s+the+Difference%3F+Why+Do+I+Need+to+Know%3F+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Seccomp and eBPF; What’s the Difference? Why Do I Need to Know?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7qb/seccomp-and-ebpf-whats-the-difference-why-do-i-need-to-know-natalia-reka-ivanko-duffie-cooley-isovalent-cisco
- YouTube search: https://www.youtube.com/results?search_query=Seccomp+and+eBPF%3B+What%E2%80%99s+the+Difference%3F+Why+Do+I+Need+to+Know%3F+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=o5MdGMFcj1M
- YouTube title: Seccomp and eBPF; What’s the Difference? Why Do I Need to Know? - Natalia Reka Ivanko, Duffie Cooley
- Match score: 0.856
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/seccomp-and-ebpf-whats-the-difference-why-do-i-need-to-know/o5MdGMFcj1M.txt
- Transcript chars: 28484
- Keywords: actually, container, policy, sensitive, application, process, tetron, kernel, profile, runtime, ebpf, running, basically, tetragon, engine, security, enforcement, advantages

### Resumo baseado na transcript

so a little introduction I'm Duffy kouy I'm the field CTO at isovalent isovalent is now part of Cisco we're still doing all the same things we were doing before we were a part of Cisco nothing's really changed for us um and we're continuing to go to market so if you ever want to hear more about psyllium ebpf tetron any of those things definitely find the guy in the Hat and ask him questions my name is Natalia I'm the product lead for runtime security at Island which

### Excerpt da transcript

so a little introduction I'm Duffy kouy I'm the field CTO at isovalent isovalent is now part of Cisco we're still doing all the same things we were doing before we were a part of Cisco nothing's really changed for us um and we're continuing to go to market so if you ever want to hear more about psyllium ebpf tetron any of those things definitely find the guy in the Hat and ask him questions my name is Natalia I'm the product lead for runtime security at Island which is now part of CIS so this is our agenda we're going to kind of introduce a few of the ideas like talking about like what is setc comp get into some evf stuff maybe do a little demon demonstration of some things and then we're going to talk about kind of the advantages and disadvantages of each technology so to get started I wanted to introduce set comp set comp is uh actually stands for secure Computing it was introduced in 2005 well before many of the other Primitives of containers right we didn't really have a lot of the other things that make up a container today and it was initially help introduced to help limit applications that were running on a server in the old style without containers um that share a kernel between each other right so like limiting that and what are they actually limiting they're limiting things like you know any application that opens a file might be I I I need to be I would need a system system call that's called open at or if you're opening a socket but there are a bunch of other system calls in that API that perhaps you wouldn't want that application to be able to have right like shutdown or reboot or like you know some of the more obvious like system calls that don't really you wouldn't really necessarily want applications that are sharing a Linux kernel to have that kind of control over over the Linux kernel it was also one of the first sandbox mechanisms and from then we've seen so many more sandboxes which is a term I absolutely love like anybody who's ever seen a Sandbox like why are they call them sandboxes but but that idea of basically trying to contain or constrain an application within within a specific scope of like what it's able to do against the shared resource has just come a long way one of the examples is like the browser based stuff right so like what web assembly a lot of these things kind of uh all sort of generated out of things like secure Computing right like that that was the beginning and we've continued to iterate continue to improve cont
