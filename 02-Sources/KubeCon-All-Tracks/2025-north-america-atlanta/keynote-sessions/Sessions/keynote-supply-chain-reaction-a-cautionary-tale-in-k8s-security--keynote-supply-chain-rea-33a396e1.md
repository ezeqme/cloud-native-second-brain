---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Keynote Sessions"
themes: ["AI ML", "Security", "Community Governance"]
speakers: ["Stacey Potter", "Manager of Community", "OpenSSF", "Adolfo García Veytia", "Founder and Engineer", "Carabiner Systems"]
sched_url: https://kccncna2025.sched.com/event/27HSy/keynote-supply-chain-reaction-a-cautionary-tale-in-k8s-security-stacey-potter-manager-of-community-openssf-adolfo-garcia-veytia-founder-and-engineer-carabiner-systems
youtube_search_url: https://www.youtube.com/results?search_query=Keynote%3A+Supply+Chain+Reaction%3A+A+Cautionary+Tale+in+K8s+Security+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Keynote: Supply Chain Reaction: A Cautionary Tale in K8s Security - Stacey Potter, Manager of Community, OpenSSF & Adolfo García Veytia, Founder and Engineer, Carabiner Systems

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[AI ML]], [[Security]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Stacey Potter, Manager of Community, OpenSSF, Adolfo García Veytia, Founder and Engineer, Carabiner Systems
- Schedule: https://kccncna2025.sched.com/event/27HSy/keynote-supply-chain-reaction-a-cautionary-tale-in-k8s-security-stacey-potter-manager-of-community-openssf-adolfo-garcia-veytia-founder-and-engineer-carabiner-systems
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote%3A+Supply+Chain+Reaction%3A+A+Cautionary+Tale+in+K8s+Security+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Keynote: Supply Chain Reaction: A Cautionary Tale in K8s Security.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27HSy/keynote-supply-chain-reaction-a-cautionary-tale-in-k8s-security-stacey-potter-manager-of-community-openssf-adolfo-garcia-veytia-founder-and-engineer-carabiner-systems
- YouTube search: https://www.youtube.com/results?search_query=Keynote%3A+Supply+Chain+Reaction%3A+A+Cautionary+Tale+in+K8s+Security+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=OdGxWBK8Jpc
- YouTube title: Keynote: Supply Chain Reaction: A Cautionary Tale in K8s Security - S. Potter & A.G. Veytia
- Match score: 0.943
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/keynote-supply-chain-reaction-a-cautionary-tale-in-k8s-security/OdGxWBK8Jpc.txt
- Transcript chars: 11718
- Keywords: security, source, projects, baseline, secure, policy, working, laughter, compromised, protect, exactly, deployment, cluster, software, actually, secret, together, practices

### Resumo baseado na transcript

Uh seems the web app pod is pegged to its CPU limit because this is a critical workload. I know we allocated 150% extra CPU capacity for this pod, but it looks like it's hitting its limit. >> For years we have been working in the shadows developing security technologies to protect against uh the threads attacking open source uh not only open source but all software in the world. [laughter] >> The only difference between us and you is that we focus on on solving security problems while you as you should um are focused on your daily work. The open source project security baseline, a framework that establishes concrete actions to secure your project. >> Ah, so it's all of you security projects working together as a team like the Avengers.

### Excerpt da transcript

Yeah, we're seeing slow responses here, too. Um, it looks like maybe we're approaching our SLO percentiles. I'm just getting to my desk to check. Uh, let me get back to you. [sighs] Walking. All right. Yeah, we're seeing slow responses, huh? Let me see. Uh what is going on here? Uh seems the web app pod is pegged to its CPU limit because this is a critical workload. I know we allocated 150% extra CPU capacity for this pod, but it looks like it's hitting its limit. Let me uh increase it temporarily while we see what's going on. Okay, I'll bump the deployment to the latest image. That should help as it's even more efficient now. Coming up online. Let's All right, let's monitor the workloads. Let's see here. Okay. >> What? No, it just swallowed all the extra CPU I just gave it. A crab. Okay, it it seems like it's exfiltrating data. Oh no, I think it's mining crypto. But why? Where? This cluster is really hardened down. What's going on? >> Oh my gosh. >> No need to worry. We are here to help. >> Oh my gosh. Elsuguro, is that you?

>> That's me, Stacey Butter. Still not important. Oh my gosh. >> What seems to be the problem? >> So, my app deployment seems to have been pawned. Apparently, someone is breaking into my CL container. It starts crypto mining shortly after my deployment is ready. >> H Let me see what I can do. >> All right. Um >> well so I don't understand because [clears throat] my network policies restrict all incoming access all credentials are handled in secrets in a secrets manager. Pods run unprivileged and arbback is quite restrictive. Um all internal traffic uses MTLS. How are they getting in? >> H All right. Let me check that container image. All right. Um okay. Let me crack open the container image and see what's in it. All right, I see. Um, so it seems that your image has a malicious payload. Let me check. How are you building your image? >> Well, here's the pipelines. You can see this app is building the image. >> Okay. All right. I see the problem. Apparently, the compiler image you're using to build your project is compromised.

Someone pushed a hacked version into the registry modified to inject the crypto miner in your app. >> So, it's my code's fault. >> Oh, no, no. Your code is totally secure. Um, by the way, your Kubernetes security jobs are amazing. The malware is flowing through your software supply chain. It means that your dependencies are compromised, but nothing is actually checking them. >> But I have a vulnerability scanner
