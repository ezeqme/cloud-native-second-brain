---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Cloud Native Experience"
themes: ["AI ML", "Community Governance"]
speakers: ["Christos Markou", "Elastic"]
sched_url: https://kccnceu2026.sched.com/event/2CW5U/to-upstream-or-not-why-becoming-the-maintainer-of-your-dependencies-matters-christos-markou-elastic
youtube_search_url: https://www.youtube.com/results?search_query=To+Upstream+or+Not%3F+Why+Becoming+the+Maintainer+of+Your+Dependencies+Matters+CNCF+KubeCon+2026
slides: []
status: parsed
---

# To Upstream or Not? Why Becoming the Maintainer of Your Dependencies Matters - Christos Markou, Elastic

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Cloud Native Experience]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Christos Markou, Elastic
- Schedule: https://kccnceu2026.sched.com/event/2CW5U/to-upstream-or-not-why-becoming-the-maintainer-of-your-dependencies-matters-christos-markou-elastic
- Busca YouTube: https://www.youtube.com/results?search_query=To+Upstream+or+Not%3F+Why+Becoming+the+Maintainer+of+Your+Dependencies+Matters+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre To Upstream or Not? Why Becoming the Maintainer of Your Dependencies Matters.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW5U/to-upstream-or-not-why-becoming-the-maintainer-of-your-dependencies-matters-christos-markou-elastic
- YouTube search: https://www.youtube.com/results?search_query=To+Upstream+or+Not%3F+Why+Becoming+the+Maintainer+of+Your+Dependencies+Matters+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=O77op1kKvaM
- YouTube title: To Upstream or Not? Why Becoming the Maintainer of Your Dependencies Matters - Christos Markou
- Match score: 0.984
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/to-upstream-or-not-why-becoming-the-maintainer-of-your-dependencies-ma/O77op1kKvaM.txt
- Transcript chars: 23750
- Keywords: source, maintainers, projects, collector, events, garden, specific, actually, components, component, ensure, vendor, receiver, eventually, deprecation, collect, useful, distribution

### Resumo baseado na transcript

So the talk is about why becoming maintainers of open source dependencies matters for us. I'm a software engineer at Elastic and I am also maintainer for the open telemetry collector control project and approver in the semantic conventions of uh some of the sematic conventions in uh open telemetry and also a CNCF ambassador. We have this recent example of the ingress engineext um ingress engineext project of the Kubernetes ecosystem which recently was announced for deprecation. So these responsibilities usually are formed uh with uh technical committees, governance committees, special interest groups uh in the Kubernetes ecosystem and the CNCF in general and maintainers are not supposed to be gatekeepers of the projects but they are mostly there to to ensure that the roles are are clear. So open telemetry is the second largest CNCF project right now and it actually is an open source for telemetry provides support for collecting metrics uh traces logs and profiles recent profiles recently and in general it is a vendor neutral telemetry collection um provides So now we uh will talk about a real story that has to do with EDOT collector and uh the collection of Kubernetes events.

### Excerpt da transcript

Good morning everyone. Thank you for coming today. It's the last day so thank you for being here. So the talk is about why becoming maintainers of open source dependencies matters for us. And who am I? My name is Christo Marco. I'm a software engineer at Elastic and I am also maintainer for the open telemetry collector control project and approver in the semantic conventions of uh some of the sematic conventions in uh open telemetry and also a CNCF ambassador. So yeah why this talk today we are here at CubeCon which is a conference which is about um open source technologies that run a significant part of our digital world. But coming here we realize that behind these technologies we have all these people that develop and maintain these technologies. So there is a question here. Should we consider about becoming these people and how we can make this happen? First let's try to understand or remind why open source is important and let's take a minute to um appreciate this meme actually which in a funny way tries to highlight a crucial reality.

So most of the times our systems our digital infrastructure might rely on technologies on open source projects that are out there. They are developed and maintained by a random person on on the other side of the planet. And this is quite important because we don't always know if these projects are uh wellmaintained or well uh staffed, right? So this becomes critical for us. And we also have uh situations where things go south. We have this recent example of the ingress engineext um ingress engineext project of the Kubernetes ecosystem which recently was announced for deprecation. Uh that project was not well staffed and the maintainers called for help. Unfortunately, this never happened. So the retirement of the project happened recently and apart from this being sad, it's also uh a great migration pain for the teams that are using this project because they need to move away from this to something else. So we arrive at the central question of this presentation. Should we engage in open-source upstream work or not?

And we will try to approach this not from a philosophical perspective. I hope so but from sharing real world insights. So let's try to understand the stakeholders and the dynamics of open source. First we have the companies and the vendors that use this open source or they build on top of open source projects and they usually hire maintain core maintainers of the open source projects so as to ensure that the
