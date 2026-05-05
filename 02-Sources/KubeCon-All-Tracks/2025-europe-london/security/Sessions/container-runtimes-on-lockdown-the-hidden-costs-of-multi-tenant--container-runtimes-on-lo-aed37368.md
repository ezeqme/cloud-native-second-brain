---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Security"
themes: ["AI ML", "Security", "Runtime Containers"]
speakers: ["Lewis Denham-Parry", "Edera", "Caleb Woodbine", "ii.nz"]
sched_url: https://kccnceu2025.sched.com/event/1txFY/container-runtimes-on-lockdown-the-hidden-costs-of-multi-tenant-workloads-lewis-denham-parry-edera-caleb-woodbine-iinz
youtube_search_url: https://www.youtube.com/results?search_query=Container+Runtimes...+on+Lockdown%3A+The+Hidden+Costs+of+Multi-tenant+Workloads+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Container Runtimes... on Lockdown: The Hidden Costs of Multi-tenant Workloads - Lewis Denham-Parry, Edera & Caleb Woodbine, ii.nz

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]], [[Runtime Containers]]
- País/cidade: United Kingdom / London
- Speakers: Lewis Denham-Parry, Edera, Caleb Woodbine, ii.nz
- Schedule: https://kccnceu2025.sched.com/event/1txFY/container-runtimes-on-lockdown-the-hidden-costs-of-multi-tenant-workloads-lewis-denham-parry-edera-caleb-woodbine-iinz
- Busca YouTube: https://www.youtube.com/results?search_query=Container+Runtimes...+on+Lockdown%3A+The+Hidden+Costs+of+Multi-tenant+Workloads+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Container Runtimes... on Lockdown: The Hidden Costs of Multi-tenant Workloads.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txFY/container-runtimes-on-lockdown-the-hidden-costs-of-multi-tenant-workloads-lewis-denham-parry-edera-caleb-woodbine-iinz
- YouTube search: https://www.youtube.com/results?search_query=Container+Runtimes...+on+Lockdown%3A+The+Hidden+Costs+of+Multi-tenant+Workloads+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=I9t7qfOjgbo
- YouTube title: Container Runtimes... on Lockdown: The Hidden Costs of Multi... Lewis Denham-Parry & Caleb Woodbine
- Match score: 0.878
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/container-runtimes-on-lockdown-the-hidden-costs-of-multi-tenant-worklo/I9t7qfOjgbo.txt
- Transcript chars: 34103
- Keywords: isolation, container, running, kernel, runtime, runtimes, containers, security, workloads, compute, within, please, access, probably, virtual, around, friends, multi-tenency

### Resumo baseado na transcript

Um thank you for all coming and uh I would like to isolate some workloads. Uh, today is my first day of wearing a kilt, and I'm doing it in front of all of you. So as we said Kubernetes is great and it's an abstraction for us to understand and manage our infrastructure. This might not be a concern when you're thinking of Kubernetes when your cluster is all the way up in the cloud, but in the cold LED light of a server room, it's a process. For example, croups help us limit the resources being used allowing us to prevent the noisy neighbor problem. Set comp and nama assist with a security posture of our container uh when it can't what it can and can't do essentially and this is a form of like filtering sys calls or to mandatory access controls.

### Excerpt da transcript

So, we're going to talk about isolation today. And why is isolation important? Well, first of all, sometimes we can have a bit too much information. So, let's sort that out by isolating part of it. And I'll pass to you, Kevin. Thank you everyone. Or uh hello or Kiora as uh as they say where I'm from. I'm from New Zealand. I'm so glad to be here. Um thank you for all coming and uh I would like to isolate some workloads. So, uh let's talk a bit about that. And hey everyone, my name is Lewis. Um, as you can see, I've got the most kick-ass flag in the world. Um, that's resembling up there. Down here resembles something different. Uh, today is my first day of wearing a kilt, and I'm doing it in front of all of you. So, I think that deserves a round of applause for the amount of fear I've had for the last four hours. We had to get one round of applause in our talk. Um, and the reason for this is because I'm an organizer for KCD Edinburgh. Uh CFP is open. Um yeah, we weren't allowed to upstage this conference this year by having it in London.

So we've moved up north. Um so please CFP open. We'd love to have you there. But we'll crack on. And by cracking on, I would like you all to stand if you can for a moment. This is turning into a magic trick. No, everyone has to stand. Please, please, please, please. Yeah, look at everyone standing. So much power. Right. This room we're in today is our node. This is for compute. This could be the bare metal machine. It could be the instance in the cloud that you've never seen before. Now, looking here now, I can see pods because I can see groups of people that I know together. And also, there's all of us together. So, you might not know people in this room before, but the concept here is is that the pods are different shapes and sizes. We got some pods that just have one person and we got pods that I'd say optimistically 20 people but um and we got some pods that require additional resources. So I got pods right at the front here that need to interact with us because we need hope and help right now. Um and then at the back of the room we got like our ephemeral pods that are coming and going like some of the pods are off in the distance.

That's fine. That's fine. But we got more coming in. Now each of you were there therefore are containers and within containers we run processes and processes are your beautiful minds with everything else going on there. So just for context if you look around the room now that's what it's lik
