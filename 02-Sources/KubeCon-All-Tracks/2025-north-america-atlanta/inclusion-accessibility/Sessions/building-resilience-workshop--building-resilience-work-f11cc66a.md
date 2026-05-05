---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Inclusion + Accessibility"
themes: ["SRE Reliability"]
speakers: []
sched_url: https://kccncna2025.sched.com/event/2AscU/building-resilience-workshop
youtube_search_url: https://www.youtube.com/results?search_query=Building+Resilience+Workshop+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Building Resilience Workshop

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Inclusion + Accessibility]]
- Temas: [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: N/A
- Schedule: https://kccncna2025.sched.com/event/2AscU/building-resilience-workshop
- Busca YouTube: https://www.youtube.com/results?search_query=Building+Resilience+Workshop+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Building Resilience Workshop.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/2AscU/building-resilience-workshop
- YouTube search: https://www.youtube.com/results?search_query=Building+Resilience+Workshop+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=OqD1BH1tXbg
- YouTube title: Building Resilience with Chaos Engineering
- Match score: 0.737
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/building-resilience-workshop/OqD1BH1tXbg.txt
- Transcript chars: 21146
- Keywords: resilience, software, ultimately, developer, developers, engineering, development, testing, failure, incident, continuous, application, basically, experiment, cost, experiments, reliability, across

### Resumo baseado na transcript

Hey everyone, good morning, good afternoon, and good evening from wherever you are today. I'm here from Harness, and I'm here to talk to you about building continuous resilience in the software delivery life cycle with chaos engineering. As engineers and leaders, we are always seeking to understand and learn how the world works. Resilience mechanisms were developed in the code and in its architecture to help a system recover, fail gracefully, or simply display an error message to the user. Not everything has to be perfect, but an error message can instruct the user why something failed or help, you know, the IT person solve the problem. Do I wait for an incident to happen to prove it, or can I test it proactively?" Some common, you know, Kubernetes failure modes.

### Excerpt da transcript

Hey everyone, good morning, good afternoon, and good evening from wherever you are today. I'm here from Harness, and I'm here to talk to you about building continuous resilience in the software delivery life cycle with chaos engineering. Ultimately, cloud-native development has enabled teams to move quickly, but it also introduces new ways for software to fail quickly. SREs, QA engineers, and developers need to work together to optimize reliability and resilience to improve developer productivity. My name is Matt Shilts, and I'm a product marketing manager at Harness. We are a modern software delivery platform for continuous integration, continuous delivery, security testing, feature flags, service reliability management with service level objectives, cloud cost management, and chaos engineering. For the For the past 20 years, I have been helping teams build reliable and resilient systems and teams across the nuclear power industry, retail and e-commerce, as well as nonprofit groups that I've been a part of locally in Minnesota.

I've enjoyed being a software engineer, product manager, and product marketing manager, and hope you enjoy this presentation today. Why am I here? I'm part of the Litmus Chaos open source community, which is an incubating CNCF project. Harness, as a sponsor, is also part of the CNCF as a silver sponsor. You may have seen me at KubeCon plus CloudNativeCon Detroit, where we had our first-ever Chaos Day in October 2022. Please feel free to contact me via email, Twitter, or LinkedIn. Ultimately, we are here because we are building and making things better. As engineers and leaders, we are always seeking to understand and learn how the world works. I talk about how building for resilience is in fact chaos engineering. Ultimately, this discipline is simply allowing us to understand how the system works and operates. This is one of my favorite quotes from Twitter from Andy Stanley who has a podcast, where he just says, "If you don't know why it's working when it's working, you won't know how to fix it when it breaks." And for me, as a prior IT administrator, um this is great cuz you know, like when I had incidents and I had to respond, if it was a brand new issue that I didn't know what it was, it was hard.

I had to dig around, I was stressed, nervous. And um but when I was able to practice failure and prepare for it, I was more confident, and ultimately, less failure occurred because I proactively planned for it. Another thing here. So
