---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "SRE Reliability", "Community Governance"]
speakers: ["Wojciech Tyczyński", "Google", "Shyam Jeedigunta", "Amazon Web Services"]
sched_url: https://kccnceu2024.sched.com/event/1Yhgs/intro-+-deep-dive-kubernetes-sig-scalability-wojciech-tyczynski-google-shyam-jeedigunta-amazon-web-services
youtube_search_url: https://www.youtube.com/results?search_query=Intro+%2B+Deep+Dive%3A+Kubernetes+SIG+Scalability+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Intro + Deep Dive: Kubernetes SIG Scalability - Wojciech Tyczyński, Google & Shyam Jeedigunta, Amazon Web Services

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Wojciech Tyczyński, Google, Shyam Jeedigunta, Amazon Web Services
- Schedule: https://kccnceu2024.sched.com/event/1Yhgs/intro-+-deep-dive-kubernetes-sig-scalability-wojciech-tyczynski-google-shyam-jeedigunta-amazon-web-services
- Busca YouTube: https://www.youtube.com/results?search_query=Intro+%2B+Deep+Dive%3A+Kubernetes+SIG+Scalability+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Intro + Deep Dive: Kubernetes SIG Scalability.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1Yhgs/intro-+-deep-dive-kubernetes-sig-scalability-wojciech-tyczynski-google-shyam-jeedigunta-amazon-web-services
- YouTube search: https://www.youtube.com/results?search_query=Intro+%2B+Deep+Dive%3A+Kubernetes+SIG+Scalability+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=bxY5Q5Eoj0s
- YouTube title: Intro + Deep Dive: Kubernetes SIG Scalability - Wojciech Tyczynski, Google
- Match score: 0.844
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/intro-deep-dive-kubernetes-sig-scalability/bxY5Q5Eoj0s.txt
- Transcript chars: 31020
- Keywords: scalability, cluster, important, control, actually, little, single, couple, number, basically, regressions, working, running, actual, happening, clusters, slo, whatever

### Resumo baseado na transcript

okay um thank you so hello everyone um my name is and I'm like six scalability TL for ever almost um uh at least that's that's my feeling um so I moved this community for eight and a half years um at this point ish so um and then today I'm going to to give this presentation about sequence k6 scalable what we are doing in six scalability um both the introduction and a little bit more of a deep dive um so let's start what we what with talking to to basically exclude the the waiting time with this like um one of the things that is happening in kubernetes currently is uh is adding that the API priority and fairness to the API server which is which is basically our overload protection um or those deployments to be created over the evenly across like five minutes or something like that um it was designed for like easy extensibility so adding new slos adding new new functionality so helper functionality should be relatively simple to do that it already

### Excerpt da transcript

okay um thank you so hello everyone um my name is and I'm like six scalability TL for ever almost um uh at least that's that's my feeling um so I moved this community for eight and a half years um at this point ish so um and then today I'm going to to give this presentation about sequence k6 scalable what we are doing in six scalability um both the introduction and a little bit more of a deep dive um so let's start what we what with talking what we are doing as part of sex scalability and there are a couple couple different categories of things so um first we Define and drive what scalability of kubernetes really is it's um as you will see in a moment like it's it's not really obvious and what are our goals um in terms of where where we would like the system to to get um based on that like we coordinate and contribute the actual improvements to to to reach those goals that we defined um we Monitor and measure the system and performance of the system to to actually see that our goals were really reached um based on based on the actual um system Behavior we protect the system from scalability regressions that's that's probably one of the most important things um and and finally we um we go to the community and consult many different many different improvements or many different features that are happening across the the whole kubernetes area one more note here is we are at least sometimes confused with like the outer scaling sick those are two different things um here we are we are focusing and sex scalability we are focusing on like the overall um performance of the system how how far you can go how how far you can push certain certain limits of kubernetes out of sync Auto scaling is focused on how to how to horizontally or vertically scale like certain aspects of the system so for example horizontal pod Auto scaling or cluster Auto skating is part of a single to scaling um and it's sometimes being confused by people so um it's not what we are doing here in six scalability um okay so let's start with the the first thing defining and driving um so what what is actually kubernetes scalability um and I think that the most important thing which is not like specific to kubernetes itself but um it's it's important to keep in mind that um we shouldn't be optimizing the system for the sake of optimizing itself um it's important like every single optimization is making the system a little bit more complex harder to debug Hardware to reason about and so on so it's im
