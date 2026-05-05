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
speakers: ["Maximilian Techritz", "Johannes Ott", "SAP SE"]
sched_url: https://kccnceu2026.sched.com/event/2CW3n/how-to-build-a-european-cloud-orchestration-platform-from-within-an-enterprise-maximilian-techritz-johannes-ott-sap-se
youtube_search_url: https://www.youtube.com/results?search_query=How+to+Build+a+European+Cloud+Orchestration+Platform+From+Within+an+Enterprise+CNCF+KubeCon+2026
slides: []
status: parsed
---

# How to Build a European Cloud Orchestration Platform From Within an Enterprise - Maximilian Techritz & Johannes Ott, SAP SE

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Maximilian Techritz, Johannes Ott, SAP SE
- Schedule: https://kccnceu2026.sched.com/event/2CW3n/how-to-build-a-european-cloud-orchestration-platform-from-within-an-enterprise-maximilian-techritz-johannes-ott-sap-se
- Busca YouTube: https://www.youtube.com/results?search_query=How+to+Build+a+European+Cloud+Orchestration+Platform+From+Within+an+Enterprise+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre How to Build a European Cloud Orchestration Platform From Within an Enterprise.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW3n/how-to-build-a-european-cloud-orchestration-platform-from-within-an-enterprise-maximilian-techritz-johannes-ott-sap-se
- YouTube search: https://www.youtube.com/results?search_query=How+to+Build+a+European+Cloud+Orchestration+Platform+From+Within+an+Enterprise+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=hR8hFht9sFA
- YouTube title: How to Build a European Cloud Orchestration Platform From With... Maximilian Techritz & Johannes Ott
- Match score: 0.901
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/how-to-build-a-european-cloud-orchestration-platform-from-within-an-en/hR8hFht9sFA.txt
- Transcript chars: 16792
- Keywords: actually, control, engineers, crossplane, operator, within, enterprise, organization, together, engineering, definitely, basically, already, application, exactly, secrets, methodology, landscape

### Resumo baseado na transcript

Hello there and welcome to our presentation of how to build a European cloud orchestration platform from within an enterprise. We basically want to share our story how we've identified a problem within our enterprise 3 years ago. Well, in order to deploy our application, we deploy them to Kubernetes. Let's grab every aspect that Johannes was talking about earlier and bring it to the Kubernetes resource model. But if we look at the CNCF landscape and way beyond in the open source ecosystem, there are already so many great tools at our hands um that help you achieve this with the Kubernetes resource model already today. Frostbin is a really powerful tool where you can like manage databases, DNS at GCP, storage at AWS again from within the control plane using um yeah crossplane providers and you can crossplane is even a framework.

### Excerpt da transcript

Hello there and welcome to our presentation of how to build a European cloud orchestration platform from within an enterprise. This talk will be definitely more relaxed. We are at the second half of the day. So sit back, relax and enjoy our story. We basically want to share our story how we've identified a problem within our enterprise 3 years ago. Um how we've open sourced our project and our methodology now donated even to the Neonos Foundation which is part of the Linux Foundation Europe. So definitely sit back, relax, and enjoy. >> Cool. Thank you, Max. Well, who are the two of us? We're coming from SAP. We are working or we are speaking here for the Neo Foundation. Johannes and Max, both software engineers. I'm also focused on the community growing inside and outside of the organization. But more importantly, we are working with a team of uh roughly 45 engineers that are fully devoted to this project. And already today, we are serving a community of roughly 500 plus stakeholders and are engaging with almost 100 plus contributors.

More importantly towards the end of this talk or throughout the talk I hope we can excite some of you here in the audience to also um make use of the methodology we're sharing here and maybe even see one or two or even more of you as contributors in this pro project. What is it that we're actually trying to mitigate? What problem are we actually trying to tackle here? And for that, let's step back for a second and look at how does a simplified software usually look like. And for that, well, you have a runtime that actually runs your application logic. You usually talk to a database. You expose your application through a domain name service. You have your secret stored in a vault. And at the end, your engineers are talking or the application your engineers are building are talking to a bunch of APIs from cutting edge clean ones to really dirty old uh legacy ones, big range that we have to cope with in order to power one application. So far so good. That's not really where our uh criticism or our our pain begins.

Let's look at how most engineering teams or many engineering teams are configuring how they're achieving exactly such a cloud landscape. And for that here at CubeCon should be quite straightforward. Well, in order to deploy our application, we deploy them to Kubernetes. There's a zillion cool tools. But then there's the database. There are all these proprietary services we just uh heard about. We see GitHub actions.
