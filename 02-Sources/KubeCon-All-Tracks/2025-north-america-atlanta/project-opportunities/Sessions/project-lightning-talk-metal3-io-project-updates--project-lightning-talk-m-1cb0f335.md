---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Project Opportunities"
themes: ["AI ML", "Community Governance"]
speakers: ["Kashif Khan", "Maintainer"]
sched_url: https://kccncna2025.sched.com/event/27d4T/project-lightning-talk-metal3io-project-updates-kashif-khan-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Metal3.io+Project+Updates+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Metal3.io Project Updates - Kashif Khan, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Kashif Khan, Maintainer
- Schedule: https://kccncna2025.sched.com/event/27d4T/project-lightning-talk-metal3io-project-updates-kashif-khan-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Metal3.io+Project+Updates+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Metal3.io Project Updates.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27d4T/project-lightning-talk-metal3io-project-updates-kashif-khan-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Metal3.io+Project+Updates+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=cTeAgJjoynw
- YouTube title: Project Lightning Talk: Metal3.io Project Updates - Kashif Khan, Maintainer
- Match score: 0.887
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-metal3-io-project-updates/cTeAgJjoynw.txt
- Transcript chars: 4053
- Keywords: cluster, actually, updates, native, management, address, provider, controller, provisioning, support, infrastructure, working, automated, growth, ecosystem, deploy, operator, towards

### Resumo baseado na transcript

I'm also working as an open source architect in Ericen software technology. But today I am here as one of the maintainers of the project metalcube.io and I'll be sharing updates of the project. Metal cube can make uh uh or deploy kubernetes cluster on top of it and it also has a integration or provider uh for the cluster API.

### Excerpt da transcript

Hello everyone, my name is Kashif Khan. Uh I am um like I wear a couple of hats. I am um co-chair of CNCF tag infrastructure. I'm also working as an open source architect in Ericen software technology. But today I am here as one of the maintainers of the project metalcube.io and I'll be sharing updates of the project. Um the synonym for me for this project is managing bare metal the Kubernetes way. And this is part of our uh ongoing journey to make bare metal infrastructure feel as native and automated as any cloud environment. So the biggest uh news since last CubeCon uh in London is that Metal Cube is now an official CNCF incubating project. That's a major milestone uh for the project recognizing the project's maturity, growth, uh stability and the trust from the cloud native ecosystem. Uh a huge thanks to all the contributors, adapters and community members who have actually made this achievement uh possible. This truly belongs to all of you. So uh those of you who aren't aware what metal cube does, it actually uh if you have a bunch of bare metals and if you want to deploy a Kubernetes cluster, metal cube actually brings Kubernetes style life cycle management to bare metal servers.

And this is how actually you can uh just represent your bare metal server using a YAML and there is a controller which actually reconciles this YAML. You have to just provide uh informations like your baseboard management controller or BMC controllers like BMC's address and uh BMC uh secret and then the MAC address and that's it. Metal cube can make uh uh or deploy kubernetes cluster on top of it and it also has a integration or provider uh for the cluster API. These are the main components of uh metal cubed. So bare metal operator is the controller that handles the provisioning and deprovisioning of the hosts. We have as I said cluster API provider metal cube which connects cluster API with with the uh we have a static IP address manager and we also have uh irononic which is the underlying engine for low-level provisioning. Um some community updates uh as you can see we have amazing community engagements uh thousands of commits and a steady growth across our repositories and it also shows like how important bare metal uh automation has become in the cloud native ecosystem.

As you can see the adopters are um like big big companies like Ericson, Red Hat, Susi, Fuyutsu, Mirantis and then there are also projects like Airship and Silva who are uh who have adopted metal cube in
