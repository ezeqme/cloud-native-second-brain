---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Application Development"
themes: ["AI ML", "Networking", "Runtime Containers"]
speakers: ["Matt Heon", "Red Hat", "Shivang K Raghuvanshi", "Podman Container Tools"]
sched_url: https://kccnceu2026.sched.com/event/2CVzI/rust-vs-go-building-a-container-network-stack-from-scratch-matt-heon-red-hat-shivang-k-raghuvanshi-podman-container-tools
youtube_search_url: https://www.youtube.com/results?search_query=Rust+Vs.+Go%3A+Building+a+Container+Network+Stack+From+Scratch+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Rust Vs. Go: Building a Container Network Stack From Scratch - Matt Heon, Red Hat & Shivang K Raghuvanshi, Podman Container Tools

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Application Development]]
- Temas: [[AI ML]], [[Networking]], [[Runtime Containers]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Matt Heon, Red Hat, Shivang K Raghuvanshi, Podman Container Tools
- Schedule: https://kccnceu2026.sched.com/event/2CVzI/rust-vs-go-building-a-container-network-stack-from-scratch-matt-heon-red-hat-shivang-k-raghuvanshi-podman-container-tools
- Busca YouTube: https://www.youtube.com/results?search_query=Rust+Vs.+Go%3A+Building+a+Container+Network+Stack+From+Scratch+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Rust Vs. Go: Building a Container Network Stack From Scratch.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVzI/rust-vs-go-building-a-container-network-stack-from-scratch-matt-heon-red-hat-shivang-k-raghuvanshi-podman-container-tools
- YouTube search: https://www.youtube.com/results?search_query=Rust+Vs.+Go%3A+Building+a+Container+Network+Stack+From+Scratch+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=05wBWDa8W-g
- YouTube title: Rust Vs. Go: Building a Container Network Stack From Scratch - Matt Heon & Shivang K Raghuvanshi
- Match score: 0.864
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/rust-vs-go-building-a-container-network-stack-from-scratch/05wBWDa8W-g.txt
- Transcript chars: 24859
- Keywords: podman, container, actually, netavark, language, conntrack, network, networking, netlink, looking, library, specific, question, containers, finally, ecosystem, enough, traffic

### Resumo baseado na transcript

I am a principal engineer at Red Hat, and I am a core maintainer of Podman. Podman is a single node container engine, meaning we have the roughly the same problem space as Docker. Uh in addition, we thought that there would be some big advantages having commonality with Kubernetes in that you could use Podman as sort of a sidecar debugging thing. We have a Docker compatible CLI, but we have Kubernetes compatible networking. CNI is meant for Kubernetes, and if we are creating workload in awkward places that no one else in the Kubernetes ecosystem is using, it is entirely fair of them to drop us. I had read all the blogs, but I was genuinely amazed when it actually did come out.

### Excerpt da transcript

All right. So, starting off, I am Matt Heon. I am a principal engineer at Red Hat, and I am a core maintainer of Podman. So, let's start off with what Podman is. Anyone heard of Podman? Show of hands, please. Oh, excellent. Love to hear it. So, we'll rush through this one. Podman is a single node container engine, meaning we have the roughly the same problem space as Docker. We are deliberately not a Kubernetes runtime. If you want to do that, you want container D or Cryo. Podman is natively rootless, meaning that you can easily run it without root privileges. It's also natively demonless. This is very interesting for embedded use cases. Means that Podman itself goes away when you're in an idle state. The only thing running is your workload. Absolutely no resources other than that. We provide a Docker compatible command line interface and a Docker compatible API, so you can easily switch over. We also have a Podman specific API, which exposes some of the things you won't see in Docker, things like quadlets and easy ability to manage containers using system D, and things like pods, which we have a similar concept of to Kubernetes.

Project originally started back in 2017. We've been CNCF sandbox since 2024, hoping for incubation at some point in the near future. All right. So, now let's talk about how Podman networking works. Initially, we use CNI. Show of hands, who knows what CNI is? All right. So, CNI is the standard network interface used by Kubernetes. It's a series of plugins with going from very basic stuff, just establishing bridge networking, to highly advanced multi-machine, what do you call it, switch networks, and yeah. So, it has a lot of capability, and it was also very well established. So, back in 2017, when we were looking to rapidly iterate, just get something out the door, it made a lot of sense for us to be using CNI. Uh in addition, we thought that there would be some big advantages having commonality with Kubernetes in that you could use Podman as sort of a sidecar debugging thing. You could run a Podman in your cluster. You could connect to the network, see what was going on. That seemed like it would have certain advantages.

Unfortunately, no one actually did that. So, kind of a waste. Also, it turns out that CNI wasn't really doing all that we needed. So, as time goes on, Podman has been a product for a couple of years now, we're feeling the need to write our own plugins because while we are actually only using about 5% of what CNI
