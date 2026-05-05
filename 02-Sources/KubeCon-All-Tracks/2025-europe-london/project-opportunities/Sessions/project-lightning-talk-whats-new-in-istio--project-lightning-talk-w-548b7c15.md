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
themes: ["AI ML", "Networking", "Community Governance"]
speakers: ["Mitch Connors", "Maintainer"]
sched_url: https://kccnceu2025.sched.com/event/1tcvB/project-lightning-talk-whats-new-in-istio-mitch-connors-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+What%27s+New+in+Istio%3F+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: What's New in Istio? - Mitch Connors, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Networking]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Mitch Connors, Maintainer
- Schedule: https://kccnceu2025.sched.com/event/1tcvB/project-lightning-talk-whats-new-in-istio-mitch-connors-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+What%27s+New+in+Istio%3F+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: What's New in Istio?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcvB/project-lightning-talk-whats-new-in-istio-mitch-connors-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+What%27s+New+in+Istio%3F+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=B7lpXPZPFoI
- YouTube title: Project Lightning Talk: What's New in Istio? - Mitch Connors, Maintainer
- Match score: 0.846
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-whats-new-in-istio/B7lpXPZPFoI.txt
- Transcript chars: 6020
- Keywords: mesh, connectivity, cluster, security, traffic, companies, microsoft, iststeo, started, observability, whether, client, server, lastly, number, already, connection, running

### Resumo baseado na transcript

I'm a principal engineer at Microsoft, but more importantly, I'm a maintainer of the ISTO project uh and have been for just about seven years now. I was asked by my colleagues to give a talk uh titled what's new in ISTSTEO, but I'm actually not great at following instructions. So whether the traffic is coming into your cluster, going out of your cluster, or bouncing around inside of your cluster, you should have the same controls over its connectivity, security, and observability. You're going to get configurable access logs distributed trace sampling. If you'd like to learn more about the ISTO project in about an hour, we're going to be starting at the far end of the conference center, level three, suites 7 through nine, our ISTO day conference. Also, if you'd like to uh learn more, this QR code will take you directly to our getting get started link online.

### Excerpt da transcript

All right, everybody, come on in. Grab a seat. My name is Mitch Connors. I'm a principal engineer at Microsoft, but more importantly, I'm a maintainer of the ISTO project uh and have been for just about seven years now. I was asked by my colleagues to give a talk uh titled what's new in ISTSTEO, but I'm actually not great at following instructions. So, I'm going to give a different talk. We're going to talk about what's ISTSTEO. So, how many of you in the room are currentto users? Okay. Okay, so I'm happy with the number, but it's about 20%. So this talk is not for anybody who just raised your hand. You all already know what's going on with STTO, but we're going to talk about what is STO, why you might want to use it, and how you can get started with it. So let's jump in. Uh STTO is a service mesh, and you've heard already this morning from a few other service mesh technologies throughout the CNCF. We are by no means the only game in town. A service mesh has three primary functions. Its job is to manage connectivity between pods.

Uh security for that connectivity and observability. Let's take these one at a time. First security uh all connection between pods. If you're running a service mesh and by I'm using the word pods here, but we should really start talking about pieces of software. Uh whether that's a pod, a VM, a WASM container, or some other thing. Uh all your traffic should be encrypted with FIPS compliant encryption algorithms. Uh it should be encrypted using frequently rotated, automatically rotated PKI credentials and integrate with the PKI solution of your choice so that you're not having to manually rotate these things and keep them up to date, secret management, etc. Those certificates and credentials should uniquely identify both the client and server cryptographically for every connection in your service mesh or in your Kubernetes cluster. Uh and that means because cryp you can use cryptography to uniquely identify client and server, you have scalable off policy enforcement. You no longer have to pass around the IP addresses as identities of every service to your data plane to let it know which IPs can talk to which other IPs.

Instead, your data plane is simply going to look at the client certificate, the server certificate, and check a list of allowed connections. So that's the security aspect. Next, let's talk about connectivity. Uh a service mesh at its heart is going to do all of your L4 and L7 load balancing controls whether you're
