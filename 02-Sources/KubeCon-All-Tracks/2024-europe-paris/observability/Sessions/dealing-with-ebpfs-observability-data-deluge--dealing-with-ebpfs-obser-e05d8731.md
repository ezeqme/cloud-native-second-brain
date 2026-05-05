---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Observability"
themes: ["Observability", "Storage Data"]
speakers: ["Anna Kapuścińska", "Isovalent"]
sched_url: https://kccnceu2024.sched.com/event/1YeN5/dealing-with-ebpfs-observability-data-deluge-anna-kapuscinska-isovalent
youtube_search_url: https://www.youtube.com/results?search_query=Dealing+with+eBPF%E2%80%99s+Observability+Data+Deluge+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Dealing with eBPF’s Observability Data Deluge - Anna Kapuścińska, Isovalent

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[Storage Data]]
- País/cidade: France / Paris
- Speakers: Anna Kapuścińska, Isovalent
- Schedule: https://kccnceu2024.sched.com/event/1YeN5/dealing-with-ebpfs-observability-data-deluge-anna-kapuscinska-isovalent
- Busca YouTube: https://www.youtube.com/results?search_query=Dealing+with+eBPF%E2%80%99s+Observability+Data+Deluge+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Dealing with eBPF’s Observability Data Deluge.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeN5/dealing-with-ebpfs-observability-data-deluge-anna-kapuscinska-isovalent
- YouTube search: https://www.youtube.com/results?search_query=Dealing+with+eBPF%E2%80%99s+Observability+Data+Deluge+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=yWB8n_e4N14
- YouTube title: Dealing with eBPF’s Observability Data Deluge - Anna Kapuścińska, Isovalent
- Match score: 0.845
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/dealing-with-ebpfs-observability-data-deluge/yWB8n_e4N14.txt
- Transcript chars: 28503
- Keywords: observability, kernel, instrumentation, applications, events, ebpf, overhead, tetragon, probes, actually, security, examples, application, tracing, understand, metrics, programs, usually

### Resumo baseado na transcript

hello everyone uh happy to be speaking here and happy to that all of you are here uh I'm Anna I work at is valent on all observability things uh related to networking and security use cases um yeah I'm a software engineer uh Building Solutions uh on top of EF for network and security visibility H and today I will talk about uh using ebpf for observability um what are common issues with this and uh show you some examples how um we see it com ebpf being commonly

### Excerpt da transcript

hello everyone uh happy to be speaking here and happy to that all of you are here uh I'm Anna I work at is valent on all observability things uh related to networking and security use cases um yeah I'm a software engineer uh Building Solutions uh on top of EF for network and security visibility H and today I will talk about uh using ebpf for observability um what are common issues with this and uh show you some examples how um we see it com ebpf being commonly used for observability uh and uh yeah common news cases we we see so uh EF is present in observability space for quite a while um and it promises a lot uh it it promises uh that we will that we will get no instrumentation uh observability we just drop in something and uh magically get observability for our applications it promises complete visibility because ebpf is running in the kernel um it sees all the applications running on the machine uh especially important in um environments like kubernetes is when uh applications can be just scheduled anywhere um and um application developers don't generally need to think about where they are running uh but ebpf uh program still can see them uh ebpf also promises low overhead of um of the visibility we are getting um and reliability and reliability is a part that's uh in my opinion a bit underappreciated um because evf programs are verified uh they to run in a caral they have to be checked that they are uh safe to run um it means that they are they are pretty reliable they are not back free of course but they are more reliable than most software ding right and uh for all of these things like uh to get observability with no instrument ation there are other approaches like we can install some um some agents we can inject some side cars but uh I'm sure many of us have experienced this Dreadful incidents that uh for example affected connectivity between site car and an application and then when we need data the most we lose them um with ebpf because programs are running in the kernel um we in general they just stay there and run uh they don't cause that that many issues as uh user space um agents or side cars that can crash uh so they uh at this extra layer of reliability so this are all things that uh if promises ask for observability uh how it works uh I assume not uh everybody is familiar uh so BPF is here for a while but uh it's most of us using indirectly and not really writing vpf code so uh short uh overview of how it works um we have a user space agent
