---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Service Mesh"
themes: ["Networking"]
speakers: ["Zahari Dichev", "Buoyant"]
sched_url: https://kccnceu2023.sched.com/event/1HyZd/life-without-sidecars-is-ebpfs-promise-too-good-to-be-true-zahari-dichev-buoyant
youtube_search_url: https://www.youtube.com/results?search_query=Life+Without+Sidecars+-+Is+eBPF%27s+Promise+Too+Good+to+Be+True%3F+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Life Without Sidecars - Is eBPF's Promise Too Good to Be True? - Zahari Dichev, Buoyant

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Service Mesh]]
- Temas: [[Networking]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Zahari Dichev, Buoyant
- Schedule: https://kccnceu2023.sched.com/event/1HyZd/life-without-sidecars-is-ebpfs-promise-too-good-to-be-true-zahari-dichev-buoyant
- Busca YouTube: https://www.youtube.com/results?search_query=Life+Without+Sidecars+-+Is+eBPF%27s+Promise+Too+Good+to+Be+True%3F+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Life Without Sidecars - Is eBPF's Promise Too Good to Be True?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyZd/life-without-sidecars-is-ebpfs-promise-too-good-to-be-true-zahari-dichev-buoyant
- YouTube search: https://www.youtube.com/results?search_query=Life+Without+Sidecars+-+Is+eBPF%27s+Promise+Too+Good+to+Be+True%3F+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=onQuRBy5rgo
- YouTube title: Life Without Sidecars - Is eBPF's Promise Too Good to Be True? - Zahari Dichev, Buoyant
- Match score: 0.921
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/life-without-sidecars-is-ebpfs-promise-too-good-to-be-true/onQuRBy5rgo.txt
- Transcript chars: 24707
- Keywords: actually, ebpf, request, kernel, sidecar, mesh, particular, effectively, resource, sidecars, resources, happening, latency, programming, question, whether, running, protocol

### Resumo baseado na transcript

hello everyone and welcome to the talk titled life without sidecars it's evpf's promise too good to be true so today I'm going to try to present my opinion on why the sidecar model is here to stay and why it is in fact the future of the service mesh so first of all who am I my name is zahari duchev and I work for buoyant the creators of linker D and if you want to reach out and ask me questions or connect you can use any of

### Excerpt da transcript

hello everyone and welcome to the talk titled life without sidecars it's evpf's promise too good to be true so today I'm going to try to present my opinion on why the sidecar model is here to stay and why it is in fact the future of the service mesh so first of all who am I my name is zahari duchev and I work for buoyant the creators of linker D and if you want to reach out and ask me questions or connect you can use any of these channels so the agenda of this talk is quite packed I hope we have enough time to cover everything first of all we are gonna focus on like what what is a service Mission why you might need one we're going to look at the three main pieces of functionality that a service mesh provides then we're going to take a look at what Linker D is we're going to also explore uh and give a bit of an overview of ebpf and in particular how it relates to Cloud native networking and then we're going to ask ourselves the question of whether ebpf can actually replace the sidecar in a service mesh and we are also going to evaluate a couple of other models that are being used in production so again like I tend to think of service meshes with respect to three main uh pieces of functionality that you get when you adopt one first of all you have observability and this is something that you want in a distributed system because you really want to know what's happening in your services so that gives you service measures gives you golden metrics across all of your services so things like HTTP and TCP level metrics request sampling and all of that on the reliability front you get retries circuit breaking automatic Canary deployments based on you know success rates of your new rollout and all these nice things to keep your systems running reliably on the security front you get automatic mtls mtls in most cases across mesh workloads and you get network traffic policies that are that can express very rich Network rules on the layer 7 protocol stack and Lincoln is just a it's a service mesh that it's very simple to use and it comes with very accessible defaults in order to get you up and running as quickly as possible and get you to production and a relatively short amount of time it uses a purpose-built micro proxy that's been specifically designed to run as a sidecar it is also a cncf graduated project that benefits from a thriving open source community and you can convince yourself of that by joining our slack or you know checking out our open issues on the GitH
