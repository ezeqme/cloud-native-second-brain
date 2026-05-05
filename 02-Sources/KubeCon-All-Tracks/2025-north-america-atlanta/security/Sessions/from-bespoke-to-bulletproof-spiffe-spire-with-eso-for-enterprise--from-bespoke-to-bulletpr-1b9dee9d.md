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
themes: ["Security"]
speakers: ["May Large", "Ivy Alkhaz", "State Farm"]
sched_url: https://kccncna2025.sched.com/event/27FVt/from-bespoke-to-bulletproof-spiffespire-with-eso-for-enterprise-zero-trust-may-large-ivy-alkhaz-state-farm
youtube_search_url: https://www.youtube.com/results?search_query=From+Bespoke+To+Bulletproof%3A+SPIFFE%2FSPIRE+With+ESO+for+Enterprise+Zero+Trust+CNCF+KubeCon+2025
slides: []
status: parsed
---

# From Bespoke To Bulletproof: SPIFFE/SPIRE With ESO for Enterprise Zero Trust - May Large & Ivy Alkhaz, State Farm

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]]
- País/cidade: United States / Atlanta
- Speakers: May Large, Ivy Alkhaz, State Farm
- Schedule: https://kccncna2025.sched.com/event/27FVt/from-bespoke-to-bulletproof-spiffespire-with-eso-for-enterprise-zero-trust-may-large-ivy-alkhaz-state-farm
- Busca YouTube: https://www.youtube.com/results?search_query=From+Bespoke+To+Bulletproof%3A+SPIFFE%2FSPIRE+With+ESO+for+Enterprise+Zero+Trust+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre From Bespoke To Bulletproof: SPIFFE/SPIRE With ESO for Enterprise Zero Trust.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FVt/from-bespoke-to-bulletproof-spiffespire-with-eso-for-enterprise-zero-trust-may-large-ivy-alkhaz-state-farm
- YouTube search: https://www.youtube.com/results?search_query=From+Bespoke+To+Bulletproof%3A+SPIFFE%2FSPIRE+With+ESO+for+Enterprise+Zero+Trust+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=EVbFeCipis8
- YouTube title: From Bespoke To Bulletproof: SPIFFE/SPIRE With ESO for Enterprise Zero... May Large & Ivy Alkhaz
- Match score: 0.941
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/from-bespoke-to-bulletproof-spiffe-spire-with-eso-for-enterprise-zero/EVbFeCipis8.txt
- Transcript chars: 26238
- Keywords: cluster, server, implementation, clusters, secret, nested, external, across, secrets, another, bespoke, available, already, course, values, config, spiffy, issues

### Resumo baseado na transcript

We're super excited to bring to you from bespoke to bulletproof spiffy spire for ESO for Enterprise Zero Trust. And I'm Ivy Alcaz and this is I'm nervous, but my name is May Large >> and we're going to bring you an awesome speech and hopefully teach you guys a bunch of good stuff today. As overall adoption was about to hit scale, we thought hm we need something highly available and highly scale scalable which led us to exploration and implementation of our nested spire solution. So first off you can see across our clusters uh it's really the typical Kubernetes out of the box spire deployment. So the private certificate authority our root CA is maintained by our information security. And then two parts that I want to point out that are actually going to be different as we get to our nested spire is we used out of the box SQL light but the problem with that is if you wipe out the storage all the mounted data is disassociated.

### Excerpt da transcript

All right, everyone. Welcome to CubeCon. Thank you so much for picking our speech today. We're super excited to bring to you from bespoke to bulletproof spiffy spire for ESO for Enterprise Zero Trust. And I'm Ivy Alcaz and this is I'm nervous, but my name is May Large >> and we're going to bring you an awesome speech and hopefully teach you guys a bunch of good stuff today. So, a little bit about us. one we like to have fun as you can see but uh I'm a lead software engineer at state farm and I was actually a full stack application engineer for a long time before I switched to platform engineering so last two years I've done platform engineering and this is actually my second cubecon so kubernetes all that was new including spiffy inspire so I actually started learning spiffy inspire in the last six months and I really am one of the examples how you can go zero to hero real quick >> I'm still a mayarge I I am currently a platform engineer at State Farm and my introduction to Spiffy Spy was really from my prior job as selling software solutions focusing on secure software supply chains with tecton chains.

So that was really my introduction to concepts like workload addestation nonfalsifiable provenence like what the what's that even and now has come full circle because now Ivy and I are part of a team responsible for our spire footprint across our cluster fleet. So it it's pretty cool. It's it's a full circle now. Yeah. So, let's get started. First off, show hands. Who has used Spire in this room? Wow. Good portion. I love it. I love it. So, this is a bit of an intermediate talk today. Um, so we're going to get into a lot of detail, but I still think it's valuable if you're just on starting on your journey or if you're partway through and all of that. So, with our journey, just to cover um why we use Spyer, we all want to get rid of static secrets, right? And then why not use the open- source CNCF tried tested zero trust solution. So that's the quick why we're using Spire. But what we really wanted to address today is how we started with an out-of-the-box implementation, our bespoke implementation and realized that we were going to have scaling issues with that.

As overall adoption was about to hit scale, we thought hm we need something highly available and highly scale scalable which led us to exploration and implementation of our nested spire solution. So to kind of show off the key components of our original implementation as you can see. So first off y
