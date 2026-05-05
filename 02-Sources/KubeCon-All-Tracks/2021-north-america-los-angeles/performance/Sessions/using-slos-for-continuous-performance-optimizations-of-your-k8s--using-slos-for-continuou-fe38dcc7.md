---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Performance"
themes: ["Observability", "SRE Reliability"]
speakers: ["Andreas Grabner", "Dynatrace"]
sched_url: https://kccncna2021.sched.com/event/lV1Q/using-slos-for-continuous-performance-optimizations-of-your-k8s-workloads-andreas-grabner-dynatrace
youtube_search_url: https://www.youtube.com/results?search_query=Using+SLOs+for+Continuous+Performance+Optimizations+of+Your+K8s+Workloads+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Using SLOs for Continuous Performance Optimizations of Your K8s Workloads - Andreas Grabner, Dynatrace

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Performance]]
- Temas: [[Observability]], [[SRE Reliability]]
- País/cidade: United States / Los Angeles
- Speakers: Andreas Grabner, Dynatrace
- Schedule: https://kccncna2021.sched.com/event/lV1Q/using-slos-for-continuous-performance-optimizations-of-your-k8s-workloads-andreas-grabner-dynatrace
- Busca YouTube: https://www.youtube.com/results?search_query=Using+SLOs+for+Continuous+Performance+Optimizations+of+Your+K8s+Workloads+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Using SLOs for Continuous Performance Optimizations of Your K8s Workloads.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV1Q/using-slos-for-continuous-performance-optimizations-of-your-k8s-workloads-andreas-grabner-dynatrace
- YouTube search: https://www.youtube.com/results?search_query=Using+SLOs+for+Continuous+Performance+Optimizations+of+Your+K8s+Workloads+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=V4ByBVARjkc
- YouTube title: Using SLOs for Continuous Performance Optimizations of Your K8s Workloads - Andreas Grabner
- Match score: 0.981
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/using-slos-for-continuous-performance-optimizations-of-your-k8s-worklo/V4ByBVARjkc.txt
- Transcript chars: 35971
- Keywords: captain, performance, metrics, patterns, number, automation, little, actually, delivery, define, specify, automatically, events, couple, distributed, analysis, important, understand

### Resumo baseado na transcript

thank you all right well first of all it's nice to see so many smiling faces this already tells you that i'm not a comedian otherwise i would be paid for better jokes my name is andy grabner or andreas carmen but please call me andy it's always easier i always say that only my mom calls me andreas if i did something rude my i'm originally from austria i actually live in austria so i also want to say thanks uh for actually allowing me to come here and

### Excerpt da transcript

thank you all right well first of all it's nice to see so many smiling faces this already tells you that i'm not a comedian otherwise i would be paid for better jokes my name is andy grabner or andreas carmen but please call me andy it's always easier i always say that only my mom calls me andreas if i did something rude my i'm originally from austria i actually live in austria so i also want to say thanks uh for actually allowing me to come here and i know a lot of international speakers that couldn't make it to kubecon i was one of the lucky ones that got an exception to travel here i've been in performance engineering for the last 20 years and i want to share a couple of things that i've learned in my life as a performance engineer especially around application performance around distributed performance but not about just like how do you do performance testing or performance engineering but really how we automate all of this and this is where captain comes into play right uh captain is a cncf sandbox project we are hopefully soon reaching incubator status and yeah i want to share with you what i've learned and how i hope i can make your life easier in case you're really interested in building and optimizing uh or building better performing systems and optimizing your systems all the links and how you reach me and how you can follow up on captain on the slide now one thing that i've learned over my last 20 years is when i do performance analysis i always look at performance patterns and i want to start with this before i go into the core part of this talk which is how we can automate performance analysis based on slo service level objectives why are performance pattern patterns important because this is what i do in my life when i analyze application performance i typically look at things like distributed traces to understand the architecture especially in distributed systems hopefully i mean for the people in the room distributed traces is something we are hopefully all aware of who is looking at distributed traces yes so this is actually a small distributed trace it starts with the front end load balancer with some legacy systems some micro services some databases some third party some load balancers and so on this is a from a company in germany called step stone i did a presentation with them a couple of years ago where they talked about how they moved to a container-based environment and how kind of their architecture changed and the reason why this
