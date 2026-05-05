---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Security"
themes: ["Security", "Kubernetes Core"]
speakers: ["Lucy Sweet", "Uber", "Sandeep Kanabar", "Gen"]
sched_url: https://kccncna2025.sched.com/event/27FZo/red-vs-blue-a-live-attacker-defender-showdown-in-kubernetes-security-lucy-sweet-uber-sandeep-kanabar-gen
youtube_search_url: https://www.youtube.com/results?search_query=Red+Vs.+Blue%3A+A+Live+Attacker-Defender+Showdown+in+Kubernetes+Security+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Red Vs. Blue: A Live Attacker-Defender Showdown in Kubernetes Security - Lucy Sweet, Uber & Sandeep Kanabar, Gen

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Lucy Sweet, Uber, Sandeep Kanabar, Gen
- Schedule: https://kccncna2025.sched.com/event/27FZo/red-vs-blue-a-live-attacker-defender-showdown-in-kubernetes-security-lucy-sweet-uber-sandeep-kanabar-gen
- Busca YouTube: https://www.youtube.com/results?search_query=Red+Vs.+Blue%3A+A+Live+Attacker-Defender+Showdown+in+Kubernetes+Security+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Red Vs. Blue: A Live Attacker-Defender Showdown in Kubernetes Security.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FZo/red-vs-blue-a-live-attacker-defender-showdown-in-kubernetes-security-lucy-sweet-uber-sandeep-kanabar-gen
- YouTube search: https://www.youtube.com/results?search_query=Red+Vs.+Blue%3A+A+Live+Attacker-Defender+Showdown+in+Kubernetes+Security+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=q6ckwAXeeew
- YouTube title: Red Vs. Blue: A Live Attacker-Defender Showdown in Kubernetes Securi... Lucy Sweet & Sandeep Kanabar
- Match score: 0.912
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/red-vs-blue-a-live-attacker-defender-showdown-in-kubernetes-security/q6ckwAXeeew.txt
- Transcript chars: 28656
- Keywords: cluster, basically, database, actually, security, create, account, resource, privileges, running, access, secure, privilege, namespace, please, working, sandeep, production

### Resumo baseado na transcript

Welcome to uh Red Versus Blue, a live attacker defender showdown of Kubernetes security. I work in platform engineering at Uber and uh within the Kubernetes project. If anyone from sick security is in the room they would kill me for saying that. So uh I have a Kubernetes cluster here that I'm just deploying my applications on and uh I'm going to deploy a new application today. Well, uh, Kubernetes gives us the ability to create containers with uh some level of capabilities. And uh what these do is they enforce something called pod security, which means that um from now on you can't make pods with uh root privileges and things like this.

### Excerpt da transcript

All right, everyone. Welcome to uh Red Versus Blue, a live attacker defender showdown of Kubernetes security. So, I'm Lucy. I work in platform engineering at Uber and uh within the Kubernetes project. I'm on the node life cycle working group where I'm one of the leads of the pro of the working group and I'm joined on stage today by Sandeep. I'm doing the slide if you see it is something like a needle in a hashtag engineer. And so what needle in a hashtag basically means is that when something breaks in production I'm often being called to find out what is the root cause. So at times I'm a developer at times I'm an SR at times I'm an observability engineer trying to find the needle in the ha and I'm also the question of the death and the heart of hearing working group I'm hearing impairment and I rely entirely on captioning so if you see the mobile in my hand I'm not checking emails I'm just trying to follow what my co speaker is speaking thank you >> I don't know if I believe that though but yeah so Um, so a few disclaimers before we do this.

This is an actual live demo. Uh, don't worry, we've robustly tested this. We've tested it one time in full. Um, [laughter] that was 2 hours ago. Uh, so hopefully the demo gods uh, grace us. If they don't, then live debugging may happen on stage. Extra content for free. Amazing. Uh we've pre-prepared uh some files and commands because otherwise we would be here for hours. Um the amount of times I've messed up basic cube cuddle commands is almost embarrassing. So instead I'm just going to paste them. And um this is not in any way once you've done this your cluster is secure forever. You have perfect Kubernetes security. If anyone from sick security is in the room they would kill me for saying that. Um this is much more of a sample of uh the ways that uh things can go wrong. So with that uh should we come over to the terminal which we have here? Uh Sandep do you want to go through what we have on the terminal here? >> Sure. Uh so everyone I think first of all you see was done the last test was done two hours back.

The last test was done only seven minutes back just before this. So for I think so for information we have a local kind is 100% offline and basically I think I could just push out the Wi-Fi to be safe because anyway the Wi-Fi is not working right. So uh I had a lot of fun preparing this offline demo. Uh and the aim of this is to educate you. So we are going to have uh some simulations and I'm going to be the
