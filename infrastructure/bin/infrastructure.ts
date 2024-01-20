#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { config } from 'dotenv';

import { InfrastructureStack } from '../lib/infrastructure-stack';
import { InfrastructurePipelineStack } from '../lib/infrastructure-pipeline-stack';

config({ path: process.env.DOTENV_CONFIG_PATH });

const app = new cdk.App();

if (['ONLY_DEV'].includes(process.env.CDK_MODE || '')) {
  new InfrastructureStack(app, `InfrastructureStack-${process.env.NODE_ENV || ''}`, {
    env: { region: 'us-east-1', account: process.env.CDK_DEFAULT_ACCOUNT },
  });
}

if (['ONLY_PROD'].includes(process.env.CDK_MODE || '')) {
  new InfrastructureStack(app, `InfrastructureStack-${process.env.NODE_ENV || ''}`, {
    env: { region: 'us-east-1', account: process.env.CDK_DEFAULT_ACCOUNT },
  });
}

if (['ONLY_PIPELINE'].includes(process.env.CDK_MODE || '')) {
  new InfrastructurePipelineStack(app, 'InfrastructurePipelineStack', {
    env: { region: 'us-east-1', account: process.env.CDK_DEFAULT_ACCOUNT },
  });
}
