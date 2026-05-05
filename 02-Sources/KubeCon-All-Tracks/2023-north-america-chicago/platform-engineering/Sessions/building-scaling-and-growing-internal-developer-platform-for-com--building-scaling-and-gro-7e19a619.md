---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Platform Engineering"
themes: ["Platform Engineering", "SRE Reliability"]
speakers: ["Joshua Bezaleel Abednego", "Giri Kuncoro", "GoTo Financial"]
sched_url: https://kccncna2023.sched.com/event/1R2md/building-scaling-and-growing-internal-developer-platform-for-companies-inside-companies-joshua-bezaleel-abednego-giri-kuncoro-goto-financial
youtube_search_url: https://www.youtube.com/results?search_query=Building%2C+Scaling%2C+and+Growing+Internal+Developer+Platform+for+Companies+Inside+Companies+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Building, Scaling, and Growing Internal Developer Platform for Companies Inside Companies - Joshua Bezaleel Abednego & Giri Kuncoro, GoTo Financial

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: Joshua Bezaleel Abednego, Giri Kuncoro, GoTo Financial
- Schedule: https://kccncna2023.sched.com/event/1R2md/building-scaling-and-growing-internal-developer-platform-for-companies-inside-companies-joshua-bezaleel-abednego-giri-kuncoro-goto-financial
- Busca YouTube: https://www.youtube.com/results?search_query=Building%2C+Scaling%2C+and+Growing+Internal+Developer+Platform+for+Companies+Inside+Companies+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Building, Scaling, and Growing Internal Developer Platform for Companies Inside Companies.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2md/building-scaling-and-growing-internal-developer-platform-for-companies-inside-companies-joshua-bezaleel-abednego-giri-kuncoro-goto-financial
- YouTube search: https://www.youtube.com/results?search_query=Building%2C+Scaling%2C+and+Growing+Internal+Developer+Platform+for+Companies+Inside+Companies+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=19vx14_Z4sw
- YouTube title: Building, Scaling, and Growing Internal Developer Platfor... Joshua Bezaleel Abednego & Giri Kuncoro
- Match score: 0.736
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/building-scaling-and-growing-internal-developer-platform-for-companies/19vx14_Z4sw.txt
- Transcript chars: 33945
- Keywords: platform, companies, infrastructure, across, engineers, product, application, clusters, already, cluster, developers, workloads, consolidation, running, company, portal, repository, acquired

### Resumo baseado na transcript

hello everyone well there's so many of you this is our very first time in Chicago we took more than 20 hours flight from our hometown in Jakarta Indonesia to be here a bit of a jetl but we are very excited to share today what we learn on growing our internal developer platform for companies inside companies my name is giri and here's my colleague Joshua both of us are infrastructure Engineers from goto Financial goto Financial is a financial arm of goto group the leading digital ecosystem in

### Excerpt da transcript

hello everyone well there's so many of you this is our very first time in Chicago we took more than 20 hours flight from our hometown in Jakarta Indonesia to be here a bit of a jetl but we are very excited to share today what we learn on growing our internal developer platform for companies inside companies my name is giri and here's my colleague Joshua both of us are infrastructure Engineers from goto Financial goto Financial is a financial arm of goto group the leading digital ecosystem in Indonesia our ecosystem provides uh various service offerings from right hailing service using motorcycle bike taxi uh service food delivery service um package delivery service e-commerce and and many others for today we are focusing mostly on the goto Financial case study when the company was just started we we created uh a product called gopay from the ground up this gopay is a digital payment uh product to serve uh the use case of our customers to enable them to pay cashless when they order services in our ecosystem gopay right now is one of the largest payment companies in Southeast Asia as the business grows the GOP engineering organization grows to more than 230 plus developers as far as across 30 different teams we maintain 30 different communities clusters across uh multiple Cloud providers and data centers these clusters became the foundation of our Cloud native infrastructure as our team grows the scale grows and the cloud native Community is moving really really fast as an infrastructure team we always want to introduce something new that we learn from the community to our infrastructure this make our infrastructure structure more and more complex every day and developers suffer from the things that we ask them to let's say bumping their hem charts there was a time when we asked them to bump Helm charts like three times a day to prepare for let's say 1.6 KUB my upgrade and and so on it took us few years to realize that we had to create platform to abstract this complex infrastructure we started building this abstraction 3 years back with two purposes first purpose was we wanted to Shield the developers from learning curve of kubernetes and its ecosystem and on the other side we as an infrastructure team uh would want to maintain and govern infrastructure easily cross our flate of kubernetes clusters so how does our platform abstraction looks like we expose an interface that developers or product Engineers use on daily basis this is nothing but a UI portal a
