---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Platform Engineering"
themes: ["Platform Engineering"]
speakers: ["Jim Bugwadia", "Nirmata", "Rachael Wonnacott", "Fidelity International"]
sched_url: https://kccncna2024.sched.com/event/1i7qS/micro-segmentation-and-multi-tenancy-the-brown-mms-of-platform-engineering-jim-bugwadia-nirmata-rachael-wonnacott-fidelity-international
youtube_search_url: https://www.youtube.com/results?search_query=Micro-Segmentation+and+Multi-Tenancy%3A+The+Brown+M%26Ms+of+Platform+Engineering+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Micro-Segmentation and Multi-Tenancy: The Brown M&Ms of Platform Engineering - Jim Bugwadia, Nirmata & Rachael Wonnacott, Fidelity International

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: United States / Salt Lake City
- Speakers: Jim Bugwadia, Nirmata, Rachael Wonnacott, Fidelity International
- Schedule: https://kccncna2024.sched.com/event/1i7qS/micro-segmentation-and-multi-tenancy-the-brown-mms-of-platform-engineering-jim-bugwadia-nirmata-rachael-wonnacott-fidelity-international
- Busca YouTube: https://www.youtube.com/results?search_query=Micro-Segmentation+and+Multi-Tenancy%3A+The+Brown+M%26Ms+of+Platform+Engineering+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Micro-Segmentation and Multi-Tenancy: The Brown M&Ms of Platform Engineering.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7qS/micro-segmentation-and-multi-tenancy-the-brown-mms-of-platform-engineering-jim-bugwadia-nirmata-rachael-wonnacott-fidelity-international
- YouTube search: https://www.youtube.com/results?search_query=Micro-Segmentation+and+Multi-Tenancy%3A+The+Brown+M%26Ms+of+Platform+Engineering+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=kAgqZkNH2wQ
- YouTube title: Micro-Segmentation and Multi-Tenancy: The Brown M&Ms of Platform Engine... J. Bugwadia, R. Wonnacott
- Match score: 0.937
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/micro-segmentation-and-multi-tenancy-the-brown-m-ms-of-platform-engine/kAgqZkNH2wQ.txt
- Transcript chars: 35001
- Keywords: platform, cluster, policies, within, namespace, policy, application, network, security, engineering, workspace, running, traffic, workloads, control, actually, multi-tenancy, segmentation

### Resumo baseado na transcript

hello everyone welcome we're going to make a quick start as we'd like to make the full use of the 35 minutes that we have firstly just wanted to say a huge thank you for joining us today at cucon uh you might have had a busy week and you might be tired and or hung over so thanks for making it to our talk this afternoon so back in the 80s Van Halen was a Powerhouse of rock and roll who were known for their extravagant performances but they

### Excerpt da transcript

hello everyone welcome we're going to make a quick start as we'd like to make the full use of the 35 minutes that we have firstly just wanted to say a huge thank you for joining us today at cucon uh you might have had a busy week and you might be tired and or hung over so thanks for making it to our talk this afternoon so back in the 80s Van Halen was a Powerhouse of rock and roll who were known for their extravagant performances but they also garnered a reputation for something a little bit more interesting and that was a peculiar backstage request now upon first hearing you might think that it's simply Rockstar divish Behavior but there was in fact method to their Madness so I have a little prop at the front so I'm going to throw these into the audience they're boxes of M&M's and their their request was that in their dressing room they wanted to have a bowl of M&M's with the very stct caveat that there could be no brown M&M's I apologize there are brown M&M's in your packet now you might be wondering why they did this because I've said that there is method to their Madness and what they realized was if the crew looking after them delivered on a bowl of M&M's it was a great indicator that they had read the contract in detail and as platform Engineers we also need to be careful about the detail in a world of distributed systems and Cloud platforms a lack of configuration or a misbehaving app can create lots of troubles VI Downstream which could ultimately lead to reputational damage or financial loss so as platform Engineers we must be Guardians of the detail or as we're calling it today the brown M&M of platform engineering so a key requirement for an internal developer platform is that they serve multiple workloads and to achieve platform engineering we'd like to talk to you today about micro segmentation and multi-tenancy the reality of platform engineering is that while it seeks to lower the barrier to entry for building your applications it also needs to balance cost with an appropriate level of security and it's therefore essential to consider how different application components running on shared infrastructure that's key are allowed to communicate with one another and then weigh up the cost of the architecture that you've chosen we've seen quite a few differing approaches to deploying kubernetes all the way from multiple single tenant clusters through to names space as a service and we're going to touch on both of these today have the lovely Jim wi
