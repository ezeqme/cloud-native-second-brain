---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Maintainer Track"
themes: ["AI ML", "Platform Engineering", "SRE Reliability", "Community Governance"]
speakers: ["Yaron Schneider", "Diagrid"]
sched_url: https://kccncna2024.sched.com/event/1hova/daprs-road-ahead-genai-apis-distributed-scheduling-at-scale-and-what-it-means-for-your-platform-yaron-schneider-diagrid
youtube_search_url: https://www.youtube.com/results?search_query=Dapr%27s+Road+Ahead%3A+GenAI+APIs%2C+Distributed+Scheduling+at+Scale+and+What+It+Means+for+Your+Platform+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Dapr's Road Ahead: GenAI APIs, Distributed Scheduling at Scale and What It Means for Your Platform - Yaron Schneider, Diagrid

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Platform Engineering]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Yaron Schneider, Diagrid
- Schedule: https://kccncna2024.sched.com/event/1hova/daprs-road-ahead-genai-apis-distributed-scheduling-at-scale-and-what-it-means-for-your-platform-yaron-schneider-diagrid
- Busca YouTube: https://www.youtube.com/results?search_query=Dapr%27s+Road+Ahead%3A+GenAI+APIs%2C+Distributed+Scheduling+at+Scale+and+What+It+Means+for+Your+Platform+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Dapr's Road Ahead: GenAI APIs, Distributed Scheduling at Scale and What It Means for Your Platform.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1hova/daprs-road-ahead-genai-apis-distributed-scheduling-at-scale-and-what-it-means-for-your-platform-yaron-schneider-diagrid
- YouTube search: https://www.youtube.com/results?search_query=Dapr%27s+Road+Ahead%3A+GenAI+APIs%2C+Distributed+Scheduling+at+Scale+and+What+It+Means+for+Your+Platform+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=d20abIZbu40
- YouTube title: Dapr's Road Ahead: GenAI APIs, Distributed Scheduling at Scale and What It Means for... Y. Schneider
- Match score: 0.974
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/daprs-road-ahead-genai-apis-distributed-scheduling-at-scale-and-what-i/d20abIZbu40.txt
- Transcript chars: 29472
- Keywords: dapper, actually, workflows, platform, basically, message, interesting, seeing, application, fairly, literally, single, support, another, caching, running, infrastructure, coming

### Resumo baseado na transcript

okay can everyone hear me yes all right let's get started thank you all for being here really excited to be here with you all for the Dapper maintainer track this is a special occasion for us we'll get to that at the end uh my name is iron Schneider I'm a Dapper core maintainer streaming Committee Member uh one of the original creators of the project um came up with that when I worked at Microsoft together with my co-founder for diagrid Mark fle I donated that to cncf

### Excerpt da transcript

okay can everyone hear me yes all right let's get started thank you all for being here really excited to be here with you all for the Dapper maintainer track this is a special occasion for us we'll get to that at the end uh my name is iron Schneider I'm a Dapper core maintainer streaming Committee Member uh one of the original creators of the project um came up with that when I worked at Microsoft together with my co-founder for diagrid Mark fle I donated that to cncf um did that about a year after I donated Kaden to cncf with red hat and um yeah I've been helping organizations adopt Dapper until today so thank you all for being here and taking an interest in Dapper so um here's some stats about the growth of the project um in 24 we've done an amazing growth uh we track the SDK growth these are all public stats you can get off of pip uh nugat you know JavaScript Maven um python for example made almost a 200% year-over-year growth um JavaScript has done 109% think of Net's really going crazy with almost 1.5 million downloads per major version and these are just the SDC that we can track through public stats um by package manager sites we're not even tracking the people using daa just with HP or GPC so the project is seeing massive massive adoption and of course as project maintainers this is what matters most to us the GitHub contributors uh the contributors are the lifeblood of the project these are the people that go and day in Day Out Create issues create docs PRS contribute um to the code um contributions do not need to be code based by the way just engaging in a GitHub comment is also a contribution which is awesome and we're seeing the community growing more and more we've released uh during this year several uh cool case studies on the cncf website you can check them out graun laabs has an incredibly interesting scenario where they use Dapper to power up a software supply chain that they have uh going internally HDFC Bank uses Dapper to process 150 million transactions uh a month Vonage also has crazy scale running Dapper across I think 100 kuet clusters if I'm not mistaken across three different clouds plus an non premises environment and now wat water uses dap workflows and actors to a very large scale um these are just some of the thousands of dapper adopters that are out there today and we're really seeing Dapper being picked up more and more by large platform teams which is kind of a flip for the uh from the initial adoption pattern that we've s
