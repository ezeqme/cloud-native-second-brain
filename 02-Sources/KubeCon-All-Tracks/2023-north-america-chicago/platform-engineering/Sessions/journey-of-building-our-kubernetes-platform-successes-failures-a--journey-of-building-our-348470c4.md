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
themes: ["AI ML", "Platform Engineering", "Kubernetes Core"]
speakers: ["Maryam Tavakkoli", "Relex Solutions"]
sched_url: https://kccncna2023.sched.com/event/1R2s0/journey-of-building-our-kubernetes-platform-successes-failures-and-valuable-lessons-learned-maryam-tavakkoli-relex-solutions
youtube_search_url: https://www.youtube.com/results?search_query=Journey+Of+Building+Our+Kubernetes+Platform%3A+Successes%2C+Failures%2C+And+Valuable+Lessons+Learned+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Journey Of Building Our Kubernetes Platform: Successes, Failures, And Valuable Lessons Learned - Maryam Tavakkoli, Relex Solutions

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: United States / Chicago
- Speakers: Maryam Tavakkoli, Relex Solutions
- Schedule: https://kccncna2023.sched.com/event/1R2s0/journey-of-building-our-kubernetes-platform-successes-failures-and-valuable-lessons-learned-maryam-tavakkoli-relex-solutions
- Busca YouTube: https://www.youtube.com/results?search_query=Journey+Of+Building+Our+Kubernetes+Platform%3A+Successes%2C+Failures%2C+And+Valuable+Lessons+Learned+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Journey Of Building Our Kubernetes Platform: Successes, Failures, And Valuable Lessons Learned.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2s0/journey-of-building-our-kubernetes-platform-successes-failures-and-valuable-lessons-learned-maryam-tavakkoli-relex-solutions
- YouTube search: https://www.youtube.com/results?search_query=Journey+Of+Building+Our+Kubernetes+Platform%3A+Successes%2C+Failures%2C+And+Valuable+Lessons+Learned+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vHaE5kNrwnU
- YouTube title: Journey Of Building Our Kubernetes Platform: Successes, Failures, And Valuable L... Maryam Tavakkoli
- Match score: 0.945
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/journey-of-building-our-kubernetes-platform-successes-failures-and-val/vHaE5kNrwnU.txt
- Transcript chars: 18542
- Keywords: platform, development, having, within, environments, change, access, changes, cluster, internal, rights, clusters, deployment, principles, second, working, testing, resource

### Resumo baseado na transcript

hello everyone welcome to cucon and Cloud native con North America 2023 thank you for spending time and attending this talk this session is prerecorded and I welcome you virtually and I am honored to present to you uh journey of building our kubernetes platform successes failures and valuable lessons learn but maybe first I can tell a bit about myself who am I I'm Mariam T I am a cloud engineer at relx Solutions relx is a supply chain and Retail uh planning platform that helps um retailers unify

### Excerpt da transcript

hello everyone welcome to cucon and Cloud native con North America 2023 thank you for spending time and attending this talk this session is prerecorded and I welcome you virtually and I am honored to present to you uh journey of building our kubernetes platform successes failures and valuable lessons learn but maybe first I can tell a bit about myself who am I I'm Mariam T I am a cloud engineer at relx Solutions relx is a supply chain and Retail uh planning platform that helps um retailers unify their planning from demand and merchandise to supply chain and operations also in my free time I sometimes write some technical articles on my medium account so feel free to find me there or on my LinkedIn and I'd be more than happy to uh get to know you and get connected so today's agenda are the following items uh I'll first give you a timeline history about our project then we will uh take a look at some technical details and project structure after that we can take a look at some statistics of usage of platform within relx then I'll uh explain about advantages that we think our platform has brought within the company and after that we can dive into the lessons that we learned during uh journey of building this platform and at the end I'll shortly mention some of our uh future plans so first is projects and timeline and history let's start from 2019 when the project was born um project was initially created for a specific internal development team that was willing to migrate their workload to kubernetes at the time as for cloud providers ozor was chosen already by management due to other reasons which was not related to kubernetes service um so it was an obvious choice for the team at the time to go with aor kuany service so a few consult Fant were hired to create the project and project was born at the end of October 2019 2020 the project was changed to be a unified kubernetes platform within the company in January I joined the company initially as a site reliability engineer uh in one of the development teams within reex in March uh there were already five different teams that started using the platform and my team was one of those in April uh there was one internal employee who joined the team uh to work uh alongside the Consultants on the project and in October a massive merge request related to the migration of service principles to aor managed identities were was merged and unly it became a major incident and a reverse of the change U was applied within tw
