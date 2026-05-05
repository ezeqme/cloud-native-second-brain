---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Project Opportunities"
themes: ["Observability"]
speakers: ["Dotan Horovits", "SIG Lead"]
sched_url: https://kccnceu2025.sched.com/event/1tcwL/project-lightning-talk-quick-intro-to-cicd-observability-with-opentelemetry-dotan-horovits-sig-lead
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Quick+Intro+to+CI%2FCD+Observability+with+OpenTelemetry+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Quick Intro to CI/CD Observability with OpenTelemetry - Dotan Horovits, SIG Lead

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Observability]]
- País/cidade: United Kingdom / London
- Speakers: Dotan Horovits, SIG Lead
- Schedule: https://kccnceu2025.sched.com/event/1tcwL/project-lightning-talk-quick-intro-to-cicd-observability-with-opentelemetry-dotan-horovits-sig-lead
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Quick+Intro+to+CI%2FCD+Observability+with+OpenTelemetry+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Quick Intro to CI/CD Observability with OpenTelemetry.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcwL/project-lightning-talk-quick-intro-to-cicd-observability-with-opentelemetry-dotan-horovits-sig-lead
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Quick+Intro+to+CI%2FCD+Observability+with+OpenTelemetry+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vpMHv-56gsk
- YouTube title: Project Lightning Talk: Quick Intro to CI/CD Observability with OpenTelemetry - Dotan Horovits
- Match score: 0.99
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-quick-intro-to-ci-cd-observability-with-opentel/vpMHv-56gsk.txt
- Transcript chars: 5267
- Keywords: semantic, conventions, attributes, pipeline, essentially, observability, cubecon, screenshot, express, within, others, interest, attribute, signals, software, metrics, context, lightning

### Resumo baseado na transcript

So, uh, let beer at CubeCon Europe 2025 and, uh, this lightning talk is about CI/CD observability with open telemetry. So, I've been talking about uh, CI/CD observability uh, for many years now. So we have the attributes and then once you have the attributes you attach the attributes to your uh uh telemetry and derive uh the relevant metrics traces and other signals. So you can see here examples for some uh work we did some work we did around metrics. So this is another area of focus for the SIG uh and much more that we we do both in terms of different signals, metrics, traces, events essentially logs uh and I mentioned before GitHub we also have receivers for GitLab working uh interest about Argo workflows, Jenkins and others.

### Excerpt da transcript

Great. So, uh, let beer at CubeCon Europe 2025 and, uh, this lightning talk is about CI/CD observability with open telemetry. And let's start with a quick, uh, history. So, I've been talking about uh, CI/CD observability uh, for many years now. Maybe some of you have heard me over at different stages, including here at CubeCon and CDCON and others. uh and about two years ago I uh raised uh an open telemetry enhancement proposal in OTP uh essentially suggesting to enhance OTEL to cover CI/CD observability and not just the production monitoring that we're probably all used to uh and this you can see here on on the screen the uh original and the OTP ultimately uh ended up with the formation of a new special interest group SIG under OTEL along with my colleague Ael Perkins who I believe is somewhere here at the audience. Um and the SIG deals with several areas. Uh the most important one the first one uh and the one that people know most is semantic conventions. Semon in short. Um how many here know what semantic conventions are with a show of hands?

Okay, not many. Uh but semantic conventions are essentially not the formal definition. It's the uh u essentially the common language for describing your telemetry whichever telemetry it is uh which attributes uh you report about your system and so on. In this case about CI/CD related uh attributes and there are several attributes or attribute groups that uh we we've tried to tackle with SIG. Uh first is the CI/CD pipelines. essentially the attributes uh denoting what a pipeline is and what happens there. You see some examples here on the on the screenshot um like the uh deployment name, pipeline result pipeline run ID and so on. Um and you can see from the screenshot you have the the attribute name that the semantic conventions defined the attribute type and other elements also how the different signals interrelate and so on. This is the semantic conventions. Other domains are how you express deployments consistently like Dora and so on. Uh there are also attributes for uh VCS versioning control systems expressing things uh about your the actions happening within your repo within your repository like when you uh make a change and so on.

Uh also when uh you have uh tests go on how to express uh them uniquely within your CI/CD pipeline runs. This is the testing side and uh also about u artifacts. Uh for those who know Salsa the supply chain levels for software they have the notion of an artifact uh and and the it's
