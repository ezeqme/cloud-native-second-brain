---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Platform Engineering"
themes: ["Platform Engineering"]
speakers: ["Sri Chandrasekaran", "Kate Klymkovska", "Spotify"]
sched_url: https://kccncna2025.sched.com/event/27Feb/harmonizing-strategy-and-engineering-lessons-learnt-in-building-a-platform-plugin-for-diverse-users-sri-chandrasekaran-kate-klymkovska-spotify
youtube_search_url: https://www.youtube.com/results?search_query=Harmonizing+Strategy+and+Engineering%3A+Lessons+Learnt+in+Building+a+Platform+Plugin+for+Diverse+Users+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Harmonizing Strategy and Engineering: Lessons Learnt in Building a Platform Plugin for Diverse Users - Sri Chandrasekaran & Kate Klymkovska, Spotify

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: United States / Atlanta
- Speakers: Sri Chandrasekaran, Kate Klymkovska, Spotify
- Schedule: https://kccncna2025.sched.com/event/27Feb/harmonizing-strategy-and-engineering-lessons-learnt-in-building-a-platform-plugin-for-diverse-users-sri-chandrasekaran-kate-klymkovska-spotify
- Busca YouTube: https://www.youtube.com/results?search_query=Harmonizing+Strategy+and+Engineering%3A+Lessons+Learnt+in+Building+a+Platform+Plugin+for+Diverse+Users+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Harmonizing Strategy and Engineering: Lessons Learnt in Building a Platform Plugin for Diverse Users.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Feb/harmonizing-strategy-and-engineering-lessons-learnt-in-building-a-platform-plugin-for-diverse-users-sri-chandrasekaran-kate-klymkovska-spotify
- YouTube search: https://www.youtube.com/results?search_query=Harmonizing+Strategy+and+Engineering%3A+Lessons+Learnt+in+Building+a+Platform+Plugin+for+Diverse+Users+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2t_Pdiu3B1E
- YouTube title: Harmonizing Strategy and Engineering: Lessons Learnt in Buildin... S. Chandrasekaran & K. Klymkovska
- Match score: 0.823
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/harmonizing-strategy-and-engineering-lessons-learnt-in-building-a-plat/2t_Pdiu3B1E.txt
- Transcript chars: 16257
- Keywords: product, plug-in, internal, engineering, strategy, scorecard, spotify, technical, platform, external, features, plugin, needed, helped, feedback, started, within, checks

### Resumo baseado na transcript

Hi everyone, my name is Shri and I'm a senior product manager at Spotify. Uh I joined platform engineering team the same year Shi did and my hobbies include long distance running and trying crazy things like skydiving and flying trapeze and almost forgot software engineering. And this is the story I love retelling because it helps users understand the problem that we are trying to solve at Spotify using the scorecard plugin. at the same time which is why the the plug-in does the tracking for us and this scorecard plug-in is designed to make sure that your your software components are maintained at high standards in line with your organization ations best practices. Um you can configure checks to pull data from different third party systems to measure different aspects of tech health such as testing, security, compliance and adoption of best practices. Uh we had many different challenges like missing integrations, migrating the existing checks and scorecards to the new style, preserving the historical data, setting up continuous integration, continous delivery, performance tuning, uh ensuring there is a feature party and so many more.

### Excerpt da transcript

Hi everyone, my name is Shri and I'm a senior product manager at Spotify. I joined the platform engineering team at Spotify in 2022. Um, my hobbies include reading and hiking. >> Hi, and my name is Kate and I'm a senior engineer at Spotify. Uh I joined platform engineering team the same year Shi did and my hobbies include long distance running and trying crazy things like skydiving and flying trapeze and almost forgot software engineering. Uh Shri and I have been living and breathing scorecards for the last three years. Uh and we'd like to share our story about the scorecard plugin we built and the lessons we learned along the way. As a product and engineering duo, we'll walk you through our experiences building the scorecard plug-in at Spotify. The plug-in is designed to provide a unifi unified experience for internal SAS and on-prem adopters. We'll share the lessons we learned balancing the diverse needs of internal and external users drawing from both product and technical perspectives. Uh, and we will also share some insights into how platform teams can externalize their internal tools effectively.

>> Hey Kate, did we remember to update the spreadsheet with the latest status on how our software components are doing? >> Shri, we stopped using spreadsheets in 2020 when we created the scorecard plugin. >> Exactly. And this is the story I love retelling because it helps users understand the problem that we are trying to solve at Spotify using the scorecard plugin. Pre scorecards at Spotify, there were about 30,000 plus software components and the number was continuing to grow. Manual methods to track and maintain these components was proving to become difficult and the scaryl looking spreadsheet that you see was what where we started from. But it had its limitations. Autonomous teams were making technical decisions without any standardization in place and this was causing a lot of tool fragmentation and this is why teams within Spotify started building um the scorecard plug-in and um humans are not really great at tracking too many things at the same time which is why the the plug-in does the tracking for us and this scorecard plug-in is designed to make sure that your your software components are maintained at high standards in line with your organization ations best practices.

>> Uh and on the right side you can see how our plug-in looks today. Much better, isn't it? Um here's what you can do with this plugin today. Um you can configure checks to pull
