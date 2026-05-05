---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Cloud Native Experience"
themes: ["AI ML", "Kubernetes Core", "SRE Reliability"]
speakers: ["Zain Malik", "Exostellar", "Nibir Bora", "Clean Compute"]
sched_url: https://kccncna2025.sched.com/event/27FZu/but-what-about-reliability-the-multi-million-dollar-kubernetes-cost-optimization-question-zain-malik-exostellar-nibir-bora-clean-compute
youtube_search_url: https://www.youtube.com/results?search_query=But+What+About+Reliability%3F+-+The+Multi-Million+Dollar+Kubernetes+Cost+Optimization+Question+CNCF+KubeCon+2025
slides: []
status: parsed
---

# But What About Reliability? - The Multi-Million Dollar Kubernetes Cost Optimization Question - Zain Malik, Exostellar & Nibir Bora, Clean Compute

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Cloud Native Experience]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Zain Malik, Exostellar, Nibir Bora, Clean Compute
- Schedule: https://kccncna2025.sched.com/event/27FZu/but-what-about-reliability-the-multi-million-dollar-kubernetes-cost-optimization-question-zain-malik-exostellar-nibir-bora-clean-compute
- Busca YouTube: https://www.youtube.com/results?search_query=But+What+About+Reliability%3F+-+The+Multi-Million+Dollar+Kubernetes+Cost+Optimization+Question+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre But What About Reliability? - The Multi-Million Dollar Kubernetes Cost Optimization Question.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FZu/but-what-about-reliability-the-multi-million-dollar-kubernetes-cost-optimization-question-zain-malik-exostellar-nibir-bora-clean-compute
- YouTube search: https://www.youtube.com/results?search_query=But+What+About+Reliability%3F+-+The+Multi-Million+Dollar+Kubernetes+Cost+Optimization+Question+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=GPo8WLCvaWw
- YouTube title: But What About Reliability? - The Multi-Million Dollar Kubernetes Cost Op... Zain Malik & Nibir Bora
- Match score: 0.931
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/but-what-about-reliability-the-multi-million-dollar-kubernetes-cost-op/GPo8WLCvaWw.txt
- Transcript chars: 33549
- Keywords: cost, reliability, cluster, control, optimization, resource, memory, platform, actually, eviction, workloads, blockers, cannot, workload, visibility, question, technical, running

### Resumo baseado na transcript

Uh I'm a engineering manager at data for the platform engineering team. >> And today we're going to be discussing a challenge more most organization face balancing costsaving with reliability. your before you know it like your application stability drops uh your reliability takes reliability takes a hit and then you know you make a quick U-turn you're back at high costs again so addressing reliability needs to be an intentional step to reducing cost isn't between cost and reliability it's between fear and understanding and once you break that ceiling of understanding understanding where your gaps are in your reliability posture your application failure modes, that's when your reliability peaks and costs saving follows immediately. It's it's an example where the risks of cost optimization are very obvious. So if any of you guys are running distributed databases like Cockroach DB, Cassandra on on on on Kubernetes that's extremely big of a for you.

### Excerpt da transcript

Hello everyone, welcome to our talk. My name is Zan Malik. I'm a principal software engineer at Access Stellar. >> Uh my name is Nibir. Uh I'm a engineering manager at data for the platform engineering team. >> And today we're going to be discussing a challenge more most organization face balancing costsaving with reliability. Business leaders have a misconception that reliability come can only be achieved at a high cost and every cost-saving initiative even though it's well-intentioned it might entail some risky proposal. Let's do an exercise together of costsaving initiatives. Let's build a cluster with multi-tenencies multi-en cluster to get better density and reduce waste. >> But wait, what about noisy neighbors? That will kill your performance. >> We got another one. Let's introduce cheaper spot nodes. Huge savings. >> Well, until your nodes disappear at 2 a.m. and you get paged. >> Well, this guy, but I cannot stop. >> So, we are going to tune workloads to exactly what they use. Super efficient. >> Well, right until they get throttled under peak load and someone comes and screams at you.

See, optimization breaks reliability. Well, why can't we just do all of these initiatives and call it a day? Huge savings and we have done our cost savings. Well, somehow you also end up with more outages and and this is the exact paradox like every efficiency gain it feels like we're fighting reliability. But are we really or are we just afraid? Exactly. We blame the wrong metrics. We are looking at the CPU utilization sitting at 20% while we are ignoring 90% of IO that is happening because fear because the fear feels safer than data. We have been trained to see waste as a reliability insurance. So this is exactly what happens right uh you start cutting cost without considering reliability. your before you know it like your application stability drops uh your reliability takes reliability takes a hit and then you know you make a quick U-turn you're back at high costs again so addressing reliability needs to be an intentional step to reducing cost isn't between cost and reliability it's between fear and understanding and once you break that ceiling of understanding understanding where your gaps are in your reliability posture your application failure modes, that's when your reliability peaks and costs saving follows immediately.

So these reliability gaps, they're real technical challenges. They're often covered in this safety blanket of overprovisioning. You guys a
