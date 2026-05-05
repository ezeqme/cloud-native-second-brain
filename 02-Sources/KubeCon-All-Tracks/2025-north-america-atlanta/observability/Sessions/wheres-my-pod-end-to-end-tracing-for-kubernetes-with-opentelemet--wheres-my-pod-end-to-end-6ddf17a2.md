---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Observability"
themes: ["Observability", "Kubernetes Core"]
speakers: ["Artem Tkachuk", "JP Phillips", "Netflix"]
sched_url: https://kccncna2025.sched.com/event/27FaO/wheres-my-pod-end-to-end-tracing-for-kubernetes-with-opentelemetry-artem-tkachuk-jp-phillips-netflix
youtube_search_url: https://www.youtube.com/results?search_query=Where%E2%80%99s+My+Pod%3F+End-to-End+Tracing+for+Kubernetes+With+OpenTelemetry+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Where’s My Pod? End-to-End Tracing for Kubernetes With OpenTelemetry - Artem Tkachuk & JP Phillips, Netflix

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Artem Tkachuk, JP Phillips, Netflix
- Schedule: https://kccncna2025.sched.com/event/27FaO/wheres-my-pod-end-to-end-tracing-for-kubernetes-with-opentelemetry-artem-tkachuk-jp-phillips-netflix
- Busca YouTube: https://www.youtube.com/results?search_query=Where%E2%80%99s+My+Pod%3F+End-to-End+Tracing+for+Kubernetes+With+OpenTelemetry+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Where’s My Pod? End-to-End Tracing for Kubernetes With OpenTelemetry.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FaO/wheres-my-pod-end-to-end-tracing-for-kubernetes-with-opentelemetry-artem-tkachuk-jp-phillips-netflix
- YouTube search: https://www.youtube.com/results?search_query=Where%E2%80%99s+My+Pod%3F+End-to-End+Tracing+for+Kubernetes+With+OpenTelemetry+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Dn0gvU2Czno
- YouTube title: Where’s My Pod? End-to-End Tracing for Kubernetes With OpenTelemetry - Artem Tkachuk & JP Phillips
- Match score: 0.915
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/wheres-my-pod-end-to-end-tracing-for-kubernetes-with-opentelemetry/Dn0gvU2Czno.txt
- Transcript chars: 30154
- Keywords: actually, trace, execution, started, containerd, instance, better, workload, tracing, specifically, running, cublet, custom, everything, context, happened, standard, migration

### Resumo baseado na transcript

Uh, we really appreciate you taking the time to come to our talk today. And if you if you look at the top of our slide, uh we have this screenshot from the movie Fight Club and the soundtrack to which is called Where is My Mind? kubernetes hasn't yet won the orchestration wars and it was based on apache msos uh and then in 2018 so a little bit later we have migrated the control plane specifically to be the one based on kubernetes as you've just heard but we left kind of the the data plane intact as JP said until the start of this year and we then had this migration and given the scale that of what I just described and the variety of worklets you might expect that the architecture is very So we kind of knew how everything works more or less and the challenge of course of this is that it's hard to maintain. As we're we're basically adopting all these new components, some of them us on the team, we have some experience running it, maybe not at this scale yet.

### Excerpt da transcript

So, good afternoon everybody. Uh, we hope you all been having a great time at CubeCon. Uh, we really appreciate you taking the time to come to our talk today. A lot of great options. So, you know, thanks for being here. I'm JP. I'm on the compute runtime team at Netflix. >> Hello. Hello. Hello. We hope it's like 3 p.m. We hope you have not cubed out yet. And is anybody coming from our control plane talk just 15 minutes ago? Raise your hands. Oh, awesome. A lot of people. I'm Artm. I also work together with JP on the compute runtime team. And if you if you look at the top of our slide, uh we have this screenshot from the movie Fight Club and the soundtrack to which is called Where is My Mind? That's kind of inspired us to name our talk Where is my pod? Where is my Anyway? Okay. Anyway, let's get actually started. All right. So our hope for this talk uh is actually that you just come away with some ideas for how observability specifically tracing can improve not only your ability but also your end users ability to answer that just never ending question like what happened right we get it all day probably every day um and so for our team uh this kind of journey really began at the the beginning of the year when we started to we're going to adopt Kubernetes right that might sound weird we've been running Kubernetes for a while Uh specifically we're talking about the cublet right so the data plane side of of um the system and so at the beginning of the year uh we had a plan to migrate all containers at Netflix from the current runtime to this new runtime uh and we want to make it use a standard standard software standard components uh but one of the most critical aspects we kind of had to answer is like what's the impact to users right at the end of the day migrations are really going to you know live or die by whether or not your users are happy Um, so early on we saw the need to confidently answer the customer questions of like they experienced something and it didn't match their expectations, right?

It's like reality is not matching up with what they're used to. And so we also knew we wanted to show off improvements, right? It's like migrations, it's like should be better, right? You should be in a better place at the end. Um so once be we began this migration uh became pretty clear we needed to be able to answer the questions and we were going to lean into observability to do that right the other question was if a workload isn't working we kind of had to kn
