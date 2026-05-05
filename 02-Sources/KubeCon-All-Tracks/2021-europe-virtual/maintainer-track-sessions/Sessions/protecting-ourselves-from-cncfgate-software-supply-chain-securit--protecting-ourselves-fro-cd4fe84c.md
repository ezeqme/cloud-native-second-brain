---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Security", "Community Governance"]
speakers: ["Andres Vega", "Emily Fox", "CNCF SIG-Security", "Jonathan Meadows", "Cyber Security at Citi"]
sched_url: https://kccnceu2021.sched.com/event/iE6j/protecting-ourselves-from-cncfgate-software-supply-chain-security-at-cncf-practices-and-tools-andres-vega-emily-fox-cncf-sig-security-jonathan-meadows-cyber-security-at-citi
youtube_search_url: https://www.youtube.com/results?search_query=Protecting+Ourselves+from+CNCFgate.+Software+Supply+Chain+Security+at+CNCF+-+Practices%2C+and+Tools+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Protecting Ourselves from CNCFgate. Software Supply Chain Security at CNCF - Practices, and Tools - Andres Vega & Emily Fox, CNCF SIG-Security & Jonathan Meadows, Cyber Security at Citi

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Security]], [[Community Governance]]
- País/cidade: Virtual / Virtual
- Speakers: Andres Vega, Emily Fox, CNCF SIG-Security, Jonathan Meadows, Cyber Security at Citi
- Schedule: https://kccnceu2021.sched.com/event/iE6j/protecting-ourselves-from-cncfgate-software-supply-chain-security-at-cncf-practices-and-tools-andres-vega-emily-fox-cncf-sig-security-jonathan-meadows-cyber-security-at-citi
- Busca YouTube: https://www.youtube.com/results?search_query=Protecting+Ourselves+from+CNCFgate.+Software+Supply+Chain+Security+at+CNCF+-+Practices%2C+and+Tools+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Protecting Ourselves from CNCFgate. Software Supply Chain Security at CNCF - Practices, and Tools.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE6j/protecting-ourselves-from-cncfgate-software-supply-chain-security-at-cncf-practices-and-tools-andres-vega-emily-fox-cncf-sig-security-jonathan-meadows-cyber-security-at-citi
- YouTube search: https://www.youtube.com/results?search_query=Protecting+Ourselves+from+CNCFgate.+Software+Supply+Chain+Security+at+CNCF+-+Practices%2C+and+Tools+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=jHR_sAYGGAw
- YouTube title: Protecting Ourselves from CNCFgate. Software Supply Cha... Andres Vega, Emily Fox & Jonathan Meadows
- Match score: 0.747
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/protecting-ourselves-from-cncfgate-software-supply-chain-security-at-c/jHR_sAYGGAw.txt
- Transcript chars: 21298
- Keywords: security, software, supply, pipeline, itself, provide, within, looking, source, dependencies, artifact, product, important, recommendations, ensure, native, working, potentially

### Resumo baseado na transcript

hello everyone and welcome we are so excited to have you join us today to talk about software supply chain security i'm emily fox i'm one of the co-chairs of the special interest group for security and the cncf with me today we have jonathan meadows of city and andres vega from vmware so why is cloud native supply chain a problem as we've seen with more and more organizations moving to the cloud they're adopting more and more cognitive projects to make that migration much smoother and easier and

### Excerpt da transcript

hello everyone and welcome we are so excited to have you join us today to talk about software supply chain security i'm emily fox i'm one of the co-chairs of the special interest group for security and the cncf with me today we have jonathan meadows of city and andres vega from vmware so why is cloud native supply chain a problem as we've seen with more and more organizations moving to the cloud they're adopting more and more cognitive projects to make that migration much smoother and easier and in many cases they are re-architecting from the ground up for the cloud meaning that they are buying into cloud native projects early and designing around them through modern software development practices and with those cloud native products and products coming more and more prevalent they're producing software with a lot of these capabilities and with more cloud-native products being developed and produced they're being used in deploying items to the cloud so it's a very circular supply chain that we have just as with traditional supply chains and supply chains in real life are complex and in the cloud and in software development they are just as complex and in some cases much harder to track and navigate because they are intangible there's no single product that exists that solves any organization supply chain problems supply chain security is complex there's all sorts of different layers whether or not you're a producer or a supplier or you're creating a raw material that you don't even know about and there's a large gap in the existing security space for cloud native producers and consumers nobody really knows what to do because they'd like to have that single product to solve all of their problems so realistically what is supply chain security about why why are we talking about this today supply chain security is about defense and depth and it's not only about the layers of different security components and configurations and checks and verifications that you're doing on your images and on your signatures and on your hashes it's also about the things that you are doing layered on top of each other commentary with the assurance requirements that you have for whatever it is that you're producing or creating as well as the risk tolerance of your organization or your project itself so why supply chain security specifically in cloud native well we wanted to create some form of documentation or instruction for the community to be able to understand more about why s
