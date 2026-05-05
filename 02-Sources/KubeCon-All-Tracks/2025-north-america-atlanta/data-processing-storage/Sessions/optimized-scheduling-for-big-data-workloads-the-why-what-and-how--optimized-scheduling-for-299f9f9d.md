---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Data Processing + Storage"
themes: ["Storage Data", "Kubernetes Core"]
speakers: ["Rahul Sharma", "Wilfred Spiegelenburg", "Cloudera"]
sched_url: https://kccncna2025.sched.com/event/27Fet/optimized-scheduling-for-big-data-workloads-the-why-what-and-how-of-k8s-schedulers-rahul-sharma-wilfred-spiegelenburg-cloudera
youtube_search_url: https://www.youtube.com/results?search_query=Optimized+Scheduling+for+Big+Data+Workloads+-+The+Why%2C+What+and+How+of+K8s+Schedulers+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Optimized Scheduling for Big Data Workloads - The Why, What and How of K8s Schedulers - Rahul Sharma & Wilfred Spiegelenburg, Cloudera

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[Storage Data]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Rahul Sharma, Wilfred Spiegelenburg, Cloudera
- Schedule: https://kccncna2025.sched.com/event/27Fet/optimized-scheduling-for-big-data-workloads-the-why-what-and-how-of-k8s-schedulers-rahul-sharma-wilfred-spiegelenburg-cloudera
- Busca YouTube: https://www.youtube.com/results?search_query=Optimized+Scheduling+for+Big+Data+Workloads+-+The+Why%2C+What+and+How+of+K8s+Schedulers+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Optimized Scheduling for Big Data Workloads - The Why, What and How of K8s Schedulers.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fet/optimized-scheduling-for-big-data-workloads-the-why-what-and-how-of-k8s-schedulers-rahul-sharma-wilfred-spiegelenburg-cloudera
- YouTube search: https://www.youtube.com/results?search_query=Optimized+Scheduling+for+Big+Data+Workloads+-+The+Why%2C+What+and+How+of+K8s+Schedulers+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_W83GgQof70
- YouTube title: Optimized Scheduling for Big Data Workloads - The Why, What... Rahul Sharma & Wilfred Spiegelenburg
- Match score: 0.831
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/optimized-scheduling-for-big-data-workloads-the-why-what-and-how-of-k8/_W83GgQof70.txt
- Transcript chars: 26866
- Keywords: scheduling, default, quotas, running, around, gpu, multiple, workloads, scheduleuler, within, priority, available, preeemption, apache, unicorn, workload, resource, another

### Resumo baseado na transcript

Thank you for attending this session last year of CubeCon in the afternoon. Um, so today we wanted to discuss um how you can optimize scheduling for large scale big data distributed jobs and um yeah, I've got a partner in crime. I lead our core platforms that run on Kubernetes both in private and public cloud. We have a bunch of data analytics uh products and applications from data warehousing, data engineering to machine learning, AI and even streaming data. Um we'll paint the landscape of the available schedulers available in the Kubernetes community today. And then we'll we'll close it out with a demo by Wilfred about Unicorn's key features.

### Excerpt da transcript

All right, welcome everyone. Thank you for attending this session last year of CubeCon in the afternoon. I'm glad you all could make it. Um, so today we wanted to discuss um how you can optimize scheduling for large scale big data distributed jobs and um yeah, I've got a partner in crime. We'll go through introductions as well in a bit. Uh but before we do that, just want to do a quick show of hands here. Um, who here has ever stared at a pending status for a job that you know is urgent? Okay, keep those hands raised if that job was a a Spark job or a machine learning AI array job. Okay, great. Okay, great to see there are some people familiar with that that situation. Um, we've all been there. We're running the most advanced high performance workloads on auler if you were using the default that was primarily designed for web applications. So today we're going to discuss why that's a problem and what the community is doing and what we are doing at cloudera with our unicornuler to fix some of those gaps in optimizing the scheduling issues for big data workloads.

So just quick introductions, my name is Rahul Sharma and I'm the director of product management at Cloudera. I lead our core platforms that run on Kubernetes both in private and public cloud. We have a bunch of data analytics uh products and applications from data warehousing, data engineering to machine learning, AI and even streaming data. And I'm joined by Wilfred. >> Yeah, Wilfred Spielenberg. I'm principal engineer. I uh do the development of Apache Unicorn and um the qual management sa um I'm part of the ASF the Apache software uh foundation as a member committed in Hadoop. I've been around in all this yarn and scheduling things for years and years. So >> all right thank you Wilfred. So we'll be covering this this presentation in three parts. The first part will be focused on just an introduction to how the the default scheduleuler works. The second part will be focused on defining some key terms about how the term gang scheduling is getting redefined a little bit in the community as well. Um we'll paint the landscape of the available schedulers available in the Kubernetes community today.

Um, and in the third part, we'll talk about the key gaps that we see in the default scheduler and how we can fix those with some of the scheduulers that are available out there, including Unicorn. And then we'll we'll close it out with a demo by Wilfred about Unicorn's key features. So, let's let's dive in
