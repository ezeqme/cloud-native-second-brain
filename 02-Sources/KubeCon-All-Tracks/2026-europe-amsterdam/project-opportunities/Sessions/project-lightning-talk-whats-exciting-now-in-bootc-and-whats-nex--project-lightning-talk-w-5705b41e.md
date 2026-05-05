---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Project Opportunities"
themes: ["AI ML", "Community Governance"]
speakers: ["Colin Walters", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFxJ/project-lightning-talk-whats-exciting-now-in-bootc-and-whats-next-colin-walters-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+What%27s+Exciting+Now+In+Bootc%2C+And+What%27s+Next%3F+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: What's Exciting Now In Bootc, And What's Next? - Colin Walters, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Colin Walters, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFxJ/project-lightning-talk-whats-exciting-now-in-bootc-and-whats-next-colin-walters-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+What%27s+Exciting+Now+In+Bootc%2C+And+What%27s+Next%3F+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: What's Exciting Now In Bootc, And What's Next?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFxJ/project-lightning-talk-whats-exciting-now-in-bootc-and-whats-next-colin-walters-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+What%27s+Exciting+Now+In+Bootc%2C+And+What%27s+Next%3F+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=txFg5kPwQvY
- YouTube title: Project Lightning Talk: What's Exciting Now In Bootc, And What's Next? - Colin Walters, Maintainer
- Match score: 0.919
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-whats-exciting-now-in-bootc-and-whats-next/txFg5kPwQvY.txt
- Transcript chars: 5521
- Keywords: container, basically, bootsie, kernel, systemd, integration, integrity, podman, bootsy, excited, nutshell, deploy, directly, update, called, projects, source, software

### Resumo baseado na transcript

So I'm super excited to talk to you guys today about what's new in Bootsie and ComposifS, two CNCF projects. Been working on free and open source software for like 27 28 years now. So you don't pay the cost of transitioning through hardware and uh kernel initialization. And of course, we're building out integration with other CNCF projects like Kurd, which orchestrates updates in your Kubernetes cluster. I'm really excited to talk about it because we have a very ambitious goal, which is basically to become a really good versioned immutable file system storage system that supports uh on disk integrity. So the the architecture in a nutshell is we split the metadata plane from the data plane.

### Excerpt da transcript

Thanks all. So I'm super excited to talk to you guys today about what's new in Bootsie and ComposifS, two CNCF projects. My name is Colin Walters. Been working on free and open source software for like 27 28 years now. Uh and the reason why is basically well, you know, we chose to make our society dependent on computers. And I just like to say I think free and open source software, what we build here is super important to make sure businesses and people stay in control. So that's what motivates me, right? Like that's why I build the technology. So let's talk about Bootsie first. uh we've been CNCF sandbox since salt lake in 2024 and just in a nutshell right with the bootc model there is a kernel a Linux kernel and a bootloadader and some other stuff in your OCI image and the idea is that you can deploy that we use OCI as a transport and you can deploy that directly to bare metal or virtual machines there's no intermediate container runtime you know none of the uh container annotations in the OCI image apply we just directly run in your Linux kernel, systemd, all that stuff.

And we're an image based update system, right? So you have transactional updates, good integration with security tools, all that stuff. And good integration with systemd as we'll see, and also good integration with podman. And you can install that container directly to a disk. So that was bootsy in a nutshell. Let's talk about bootsy features. So one of the things I like is we add a good integration with systemd soft reboots. The idea is you're running your image, you've built your OS, but now you want to deploy a new update. If you didn't change any kernel state, basically boots can prepare the next route and cue it for systemd to switch route to it. So you don't pay the cost of transitioning through hardware and uh kernel initialization. So that's nice. We also have uh a new tool called system reinstall bootsy that helps you uh convert an existing system a running one into a bootsy system which is uh very handy for some uh brownfield work. And of course, we're building out integration with other CNCF projects like Kurd, which orchestrates updates in your Kubernetes cluster.

I had someone tell me Bootsie and Kurd, hopefully I'm pronouncing that right, just works. And there's a lot more. But let's dive in. So that was Bootsie. Something that is brand new since uh as of pretty recently is called BCVK. And basically the idea is it's Bootsie Virtualization Kit. So the idea is you have a
