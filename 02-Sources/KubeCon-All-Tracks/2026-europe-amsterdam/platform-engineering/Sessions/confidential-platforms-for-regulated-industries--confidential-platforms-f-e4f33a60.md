---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Platform Engineering"
themes: ["Platform Engineering"]
speakers: ["William Rizzo", "Mirantis"]
sched_url: https://kccnceu2026.sched.com/event/2CW45/confidential-platforms-for-regulated-industries-william-rizzo-mirantis
youtube_search_url: https://www.youtube.com/results?search_query=Confidential+Platforms+for+Regulated+Industries+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Confidential Platforms for Regulated Industries - William Rizzo, Mirantis

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: Netherlands / Amsterdam
- Speakers: William Rizzo, Mirantis
- Schedule: https://kccnceu2026.sched.com/event/2CW45/confidential-platforms-for-regulated-industries-william-rizzo-mirantis
- Busca YouTube: https://www.youtube.com/results?search_query=Confidential+Platforms+for+Regulated+Industries+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Confidential Platforms for Regulated Industries.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW45/confidential-platforms-for-regulated-industries-william-rizzo-mirantis
- YouTube search: https://www.youtube.com/results?search_query=Confidential+Platforms+for+Regulated+Industries+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=id111CIDa6k
- YouTube title: Confidential Platforms for Regulated Industries - William Rizzo, Mirantis
- Match score: 0.883
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/confidential-platforms-for-regulated-industries/id111CIDa6k.txt
- Transcript chars: 18784
- Keywords: cluster, runtime, clusters, control, confidential, hardware, systems, nothing, mutating, images, necessarily, environment, flux, admission, already, whatever, everything, chyros

### Resumo baseado na transcript

So what we are going to go through is um what started as an experiment for a challenge. So the challenge was to well the initial request was to maximize the utilization of very expensive hardware destined to trading uh during something like six hours or so. So the uh so there is obviously regulatory burden as I said there is also a bunch of uh problem with fragmented tooling that we might have we might might not have in financial uh services for but this this last two I would say So it's a is a project is a project within the kubernetes sig uh and is to provide um a set of API namely tree infrastructure provider control plane provider and bootstrap provider for declarative declaratively uh create clusters from a managed a managed or unmanaged Kubernetes cluster. So going back in the architecture we have uh Amirant's uh open source project called Cordant uh which is what we like to call a platform control plane uh and cordant uh unify the man the state management and the cluster management and optionally the observability of the entire state uh through copy. So we would have containerd obviously and we have we have focused on k0 but we can do this with any type of kubernetes engine.

### Excerpt da transcript

So what we are going to go through is um what started as an experiment for a challenge. So the challenge was to well the initial request was to maximize the utilization of very expensive hardware destined to trading uh during something like six hours or so. dur uh this talk was I apologize this talk if you looked at it at the beginning of of the when the schedule was announced uh we were supposed to be two um myself and another person uh and this other person a good friend and a fantastic engineer uh worked for the regulated industry for the regulator firm that we are talking about and we designed this pretty much at forens uh for reasons that we're not going to go through he could not make it. Uh but Eric, we wish you were here. So the initial challenge was to maximize the utilization of this very expensive hardware and find a way to uh to en encapsulate K0. Uh everyone knows K0. No really lightweight Kubernetes engine like it's the best there is. Okay, whatever. CNCF project. um the to encapsulate the the K0S binary and everything that is used to use these systems that are under audit.

So uh and then somehow uh remove this this encapsulation let's call it like this now and um uh for the for the for the software that does the audit before the start of the trading that everything is clean. So this is this is the premise. So my name is William Ritzo. Uh I am a a global field CTO at Mirantis. I'm in the Kubernetes release team. Uh I'm a CNCF ambassador linker ambassador and I'm a Chyros maintainer. Specifically I work in Chyros. I work on the uh cluster API provider integration. Uh and I'm a member contributor in Fenos the open source in finance foundation. So as I said uh we had uh something like 10,000 systems approximately we still have something like 10,000 systems that are very expensive and the re the demand was how can we maximize the capital expenditure that we have on these systems. These systems are working for six hours a day and then for the rest of the day they're doing nothing but they are under audit. So if something is uh not aligned with how the auditor are expected to find the systems then they have to be t taken out of the trading pool.

Sounds familiar to anyone? Not at all. Okay. One guy. Okay. So the uh so there is obviously regulatory burden as I said there is also a bunch of uh problem with fragmented tooling that we might have we might might not have in financial uh services for but this this last two I would say that is not necessa
