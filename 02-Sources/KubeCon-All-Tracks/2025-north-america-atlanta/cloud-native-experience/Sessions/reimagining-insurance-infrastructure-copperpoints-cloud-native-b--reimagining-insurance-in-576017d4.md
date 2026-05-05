---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Cloud Native Experience"
themes: ["Cloud Native Experience"]
speakers: ["Sid Dixit", "Sham Rao", "CopperPoint Insurance Companies"]
sched_url: https://kccncna2025.sched.com/event/27FX0/reimagining-insurance-infrastructure-copperpoints-cloud-native-blueprint-sid-dixit-sham-rao-copperpoint-insurance-companies
youtube_search_url: https://www.youtube.com/results?search_query=Reimagining+Insurance+Infrastructure%3A+CopperPoint%27s+Cloud+Native+Blueprint+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Reimagining Insurance Infrastructure: CopperPoint's Cloud Native Blueprint - Sid Dixit & Sham Rao, CopperPoint Insurance Companies

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Cloud Native Experience]]
- Temas: [[Cloud Native Experience]]
- País/cidade: United States / Atlanta
- Speakers: Sid Dixit, Sham Rao, CopperPoint Insurance Companies
- Schedule: https://kccncna2025.sched.com/event/27FX0/reimagining-insurance-infrastructure-copperpoints-cloud-native-blueprint-sid-dixit-sham-rao-copperpoint-insurance-companies
- Busca YouTube: https://www.youtube.com/results?search_query=Reimagining+Insurance+Infrastructure%3A+CopperPoint%27s+Cloud+Native+Blueprint+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Reimagining Insurance Infrastructure: CopperPoint's Cloud Native Blueprint.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FX0/reimagining-insurance-infrastructure-copperpoints-cloud-native-blueprint-sid-dixit-sham-rao-copperpoint-insurance-companies
- YouTube search: https://www.youtube.com/results?search_query=Reimagining+Insurance+Infrastructure%3A+CopperPoint%27s+Cloud+Native+Blueprint+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=jQRpHOm4Vts
- YouTube title: Reimagining Insurance Infrastructure: CopperPoint's Cloud Native Blueprint - Sid Dixit & Sham Rao
- Match score: 0.963
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/reimagining-insurance-infrastructure-copperpoints-cloud-native-bluepri/jQRpHOm4Vts.txt
- Transcript chars: 25091
- Keywords: architecture, pretty, copper, systems, vendor, probably, everything, simple, another, journey, cloudnative, integration, cost, donkey, secrets, insurance, infrastructure, native

### Resumo baseado na transcript

We are going to keep it very simple and we are going to talk about Copper Point's cloud native blueprint specifically from an insurance angle. I'm a principal architect at Copper Point along with Shamar Rao and we are going to talk about the cloud native journey that we have been through as a part of copper point insurance. We want to make sure that while we are doing all of that we want to not only focus on revenue but also remain cost effective. We wanted to adhere to all the principles including containerization microservices composible and event-driven design as a part of our architecture to support good customer experience. But we also run a lot of our jobs as a part of plain vanilla Kubernetes uh chron expressions. We not only uh we not only uh you know reduce our incremental cost as we go cloud native we accelerate our time to go to market time to market um we are able to provide real-time streaming data and this is particularly important now

### Excerpt da transcript

Good evening everyone. Um I know it's very late during the day. I'm sure the caffeine is wearing out for you guys but bear with me. Uh it's going to be a very straightforward session. We are going to keep it very simple and we are going to talk about Copper Point's cloud native blueprint specifically from an insurance angle. My name is Sid Dixit. I'm a principal architect at Copper Point along with Shamar Rao and we are going to talk about the cloud native journey that we have been through as a part of copper point insurance. So the insurance industry isn't like a move fast break things kind of a industry. It's a regulated industry. We deal with a lot of sensitive data. We deal with a lot of you know auditors. We are accountable to auditors. We are accountable accountable to regulators. We are accountable to policyh holders and agents, right? But that doesn't mean that we as an organization ignore modern architecture. What it means as a part of as a part of our cloudnative strategy uh or as a part of our cloudnative story, our systems have to be designed to handle compliance, has to be designed to handle resilience and has to be built upon trust.

Before we move further, I think it'll be helpful to talk about who we are. This is our first uh you know presentation at CubeCon. So it'll be helpful for us to know what Copper Point is and who we are, right? We are an insurance company. We started as a single state, single line of business, state fund out of Phoenix, Arizona, workers compensation line of business back in uh 1925, way before I was born. Right. In 2017 uh we acquired uh Pacific Compensation. Before that we also became privatized and then we we started uh we became a mutual company uh called Corporate Point Insurance Company. And in 2017 we started a journey of expansion. We acquired Pacific Compensation which allowed us to expand our business to multiple states including California. In 2019, we acquired Alaska National Corporation and that allowed us to grow organically across different business lines other than workers compensation, right? Be it property, be it commercial, auto. So we in 20 2019 after acquiring Alaska National, we we started expanding further.

It was not until 2023 we decided to move all our infrastructure our our workloads from on-prem to cloud and we completed our integration of all of these systems and all of these acquisitions that we did in the last few years right and 2025 is the year when we are celebrating our 100th anni
