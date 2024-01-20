/* ---------- External libraries ---------- */
import { Stack, StackProps, Tags } from 'aws-cdk-lib';
import { IRepository } from 'aws-cdk-lib/aws-ecr';
import { IBaseService } from 'aws-cdk-lib/aws-ecs';
import { IBucket } from 'aws-cdk-lib/aws-s3';
import { Construct } from 'constructs';

/* ---------- Constructs ---------- */
import { PipelineStack } from './constructs/Pipeline/index';

interface PipelineProps extends StackProps {
  bucket?: IBucket;
  repository?: IRepository;
  expressAppService?: IBaseService;
}

export class InfrastructurePipelineStack extends Stack {
  constructor(scope: Construct, id: string, props: PipelineProps) {
    super(scope, id, props);

    /* ---------- Constructs ---------- */
    new PipelineStack(this, 'Infrastructure-Pipeline-Prod', {
      environment: 'Production',
    });

    new PipelineStack(this, 'Infrastructure-Pipeline-Dev', {
      environment: 'Development',
    });

    /* ---------- Tags ---------- */
    Tags.of(scope).add('Project', 'Infrastructure-Pipeline');
  }
}
