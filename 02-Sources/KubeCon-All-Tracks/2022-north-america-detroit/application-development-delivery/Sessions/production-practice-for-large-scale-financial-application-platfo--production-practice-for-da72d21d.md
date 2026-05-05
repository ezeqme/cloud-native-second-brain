---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Application + Development + Delivery"
themes: ["Platform Engineering", "GitOps Delivery", "SRE Reliability"]
speakers: ["Jiahang Xu", "China Merchants Bank", "Jianbo Sun", "Alibaba Cloud"]
sched_url: https://kccncna2022.sched.com/event/182D2/production-practice-for-large-scale-financial-application-platform-in-china-merchants-bank-jiahang-xu-china-merchants-bank-jianbo-sun-alibaba-cloud
youtube_search_url: https://www.youtube.com/results?search_query=Production+Practice+For+Large-Scale+Financial+Application+Platform+In+China+Merchants+Bank+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Production Practice For Large-Scale Financial Application Platform In China Merchants Bank - Jiahang Xu, China Merchants Bank & Jianbo Sun, Alibaba Cloud

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Application + Development + Delivery]]
- Temas: [[Platform Engineering]], [[GitOps Delivery]], [[SRE Reliability]]
- País/cidade: United States / Detroit
- Speakers: Jiahang Xu, China Merchants Bank, Jianbo Sun, Alibaba Cloud
- Schedule: https://kccncna2022.sched.com/event/182D2/production-practice-for-large-scale-financial-application-platform-in-china-merchants-bank-jiahang-xu-china-merchants-bank-jianbo-sun-alibaba-cloud
- Busca YouTube: https://www.youtube.com/results?search_query=Production+Practice+For+Large-Scale+Financial+Application+Platform+In+China+Merchants+Bank+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Production Practice For Large-Scale Financial Application Platform In China Merchants Bank.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182D2/production-practice-for-large-scale-financial-application-platform-in-china-merchants-bank-jiahang-xu-china-merchants-bank-jianbo-sun-alibaba-cloud
- YouTube search: https://www.youtube.com/results?search_query=Production+Practice+For+Large-Scale+Financial+Application+Platform+In+China+Merchants+Bank+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ye5kKn7RyFc
- YouTube title: Production Practice For Large-Scale Financial Application Platform In...- Jiahang Xu & Jianbo Sun
- Match score: 0.942
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/production-practice-for-large-scale-financial-application-platform-in/ye5kKn7RyFc.txt
- Transcript chars: 16387
- Keywords: application, dashboard, add-ons, define, components, definition, deploy, add-on, calorie, version, clickhouse, component, install, instance, traffic, control, already, important

### Resumo baseado na transcript

hi everyone um from China Merchants Bank I will give a brief introduction for myself I have a 13 years software research and development experience across Telecom Automotive Financial industry recently here I focused on quality of resourcing knowledge and take some in practice currently I'm responsible for both Cloud native application plan for in China Merchants Bank I'm glad to have a chance to share our Enterprise practice experience six so let's start okay today's topic is about the production practice for large-scale financial application platform in China mattress their demo demo app the same name app they will generate log Trace metrics of the APB so this Observer observability data will be encoded as Hotel and connect it to time Siri database change database and colon storage for allies and the dashboard if

### Excerpt da transcript

hi everyone um from China Merchants Bank I will give a brief introduction for myself I have a 13 years software research and development experience across Telecom Automotive Financial industry recently here I focused on quality of resourcing knowledge and take some in practice currently I'm responsible for both Cloud native application plan for in China Merchants Bank I'm glad to have a chance to share our Enterprise practice experience six so let's start okay today's topic is about the production practice for large-scale financial application platform in China mattress bag and this step I will appear with these Jim bosson a staff engineer Alibaba clouds is by also is my friends um most of us are the cool Villa maintainer today's agendas includes four parts backgrounds practice in CMB zombie is a short name of my company in a Villa Cuba Villa in central feature introduction and we'll show a demo about the feature the first two parts I will charge the part three and part four uh jumbo will take on charge okay let me give a brief introduction about China Merchants Bank Channel Merchants Bank is a commercial best bank ranking as 14th of the World Bank in last year's 2021 uh there are two merger um mobile apps App Store a mobile here check and CMB life both over apps has large skill customers globally until end of June mobile Bank app has already 1178 million customer Global 7B live has um 32 million also so uh China Merchants Bank has developed a reputation for being a technology folks banking globally where I'll wait to Cloud native we really change in application domain um in recent year we has already established a large-scale private cloud in our organization from the high level private Cloud architecture diagram we can notice there are Apple wider virtual machine kubernetes serverless Hadoop and some decades runtimes and huge infrastructure in the we provide diverged foreclosed and the middleware service in corresponding domain a corresponding on time applications couples with runtime and infrastructure it's really complex and challenge for us Devils cannot be agile and cannot be high efficiency so both application engineer and the plan for engineer have some some issue to be resolved from application engineer size they want to decouple application from wrong time or infrastructure and also one application and support Academy delivery to make the penis stable ability and the security and one application observability for maintenance and the plan for engi
